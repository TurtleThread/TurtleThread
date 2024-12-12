import os 
import tempfile 
from matplotlib import font_manager 
from fuzzywuzzy import process, fuzz 
from pathlib import Path 

from opentypesvg import fonts2svg 

from .draw_svg import drawSVG 



# make it possible to at runtime process text 

class Fonts2SVGFakeOptions():
    def __init__(self, fontpath, outfolder):
        self.colors_list = ['#ffffff']
        self.output_folder_path = outfolder
        self.gnames_to_generate = []
        self.gnames_to_add = []
        self.gnames_to_exclude = []
        self.glyphsets_union = False
        self.adjust_view_box_to_glyph = False
        self.input_paths = [fontpath]
        self.font_paths_list = fonts2svg.validate_font_paths(self.input_paths)



class LetterDrawer(): 
    letter_gap = 0.03 
    line_spacing = 1.15 

    def __init__(self, turtle, load_common_fonts:bool=False): 
        self.turtle = turtle 

        self.loaded_fonts = {} 
        self.created_tmpdirs = [] 
        # equivalent to self.clear_fonts() 

        if load_common_fonts: 
            try: 
                self.load_font('Arial') 
            except: 
                pass 
            try: 
                self.load_font("Helvetica") 
            except: 
                pass 
            try: 
                self.load_font("Comic") # comic sans 
            except: 
                pass 


    # context manager functions 
    def __enter__(self): 
        return self 

    def __exit__(self, type, value, traceback): 
        self.clear_fonts() # this will delete the temp directories with the .svg files 
        return False # don't suppress the errors 
    

    font_search_score_threshold = 90 
    # if we want to use .otf or whatever font files 
    def load_font(self, fontname:str, fontpath:str=None, search_threshold=None): 
        # Loads a font file from a fontpath, and gives it a name to be referred to. 
        # if no fontpath specified, will try to find it in system files 

        if fontpath is None: 
            # set search threshold 
            if search_threshold is None: 
                search_threshold = LetterDrawer.font_search_score_threshold 

            # get system fonts 
            fontpaths = font_manager.findSystemFonts(fontpaths=None, fontext='otf')
            fontnames = [Path(fp).name.lower() for fp in fontpaths] 
            res_ttf = process.extract(fontname.lower()+".ttf", fontnames, scorer=fuzz.ratio) 
            res_otf = process.extract(fontname.lower()+".otf", fontnames, scorer=fuzz.ratio) 
            for filename, score in res_ttf + res_otf: 
                if score >= search_threshold: 
                    # THIS IS A GOOD ENOUGH MATCH! 
                    fontpath = fontpaths[fontnames.index(filename)] 
                    break 
        
        if fontpath is None: # means it couldn't be found from previously 
            raise ValueError("Could not find font in system files: "+str(res_ttf+res_otf)) 


        td = tempfile.TemporaryDirectory() 
        self.created_tmpdirs.append(td) 
        tmpdirname = td.name 

        # processs text format: convert to svg first 

        opts = Fonts2SVGFakeOptions(fontpath=fontpath, outfolder=tmpdirname)
        font_paths_list = opts.font_paths_list
        hex_colors_list = opts.colors_list

        output_folder_path = fonts2svg.get_output_folder_path(opts.output_folder_path,
                                                        font_paths_list[0])

        fonts2svg.processFonts(font_paths_list, hex_colors_list, output_folder_path, opts) 
        # font SVGs are now in tmpdirname 


        # get the paths to the font SVGs 
        paths = {}
            
        for rt, _, files in os.walk(tmpdirname):
            for i in range(len(files)):
                try: 
                    paths[files[i][:files[i].index('.svg')]] = os.path.join(rt, files[i])
                except ValueError as ve: 
                    print("WARNING (GETTING SVGS):", ve) 

        self.loaded_fonts[fontname] = paths 

        return fontpath 
    
    def get_loaded_fontnames(self): 
        # get a list of names of fonts that are already loaded 
        return list(self.loaded_fonts.keys()) 


    def draw_one_letter(self, fontname, lettername, fontsize=20, colour='#000000', thickness=1, fill=True, outline=False, turtle=None, flip_y=False): # TODO support changing colours 
        # draws one letter with the turtles, with the specified fields. 
        # turtle defaults to self.turtle 
        if turtle is None: 
            if self.turtle is None: 
                raise ValueError("MUST DECLARE turtle TO USE IN LetterDrawer.draw_one_letter in either draw_one_letter() or LetterDrawer() init") 
            turtle = self.turtle 
        
        #print("DRAWING LETTER", lettername)

        if lettername == 'space': 
            currpos = list(turtle.position())
            # move right a bit 
            with turtle.jump_stitch(): 
                turtle.goto(currpos[0]+fontsize, currpos[1]) 
            return 
        
        # DRAW ONE LETTER OF A FONT WITH A LOADED NAME, GIVEN A COLOUR 
        if fontname in self.loaded_fonts.keys(): 
            try: 
                drawSVG(turtle, self.loaded_fonts[fontname][lettername], fontsize, colour, thickness, fill, outline, flip_y) 
                #print("DREW SVG")
            except Exception as e: 
                print("OR, it might be some other error({})".format(e))
                raise ValueError("font '{}' does not have the letter '{}'".format(fontname, lettername)) 
               
        else: 
            raise ValueError("font '{}' not loaded".format(fontname))
        
        return 
    
    def draw_letter_gap(self, fontsize, letter_gap=None): 
        if letter_gap is None: 
            letter_gap = LetterDrawer.letter_gap 
        #print("DRAWING LETTER GAP")
        # this draws the gap between two letters (not whitespace) 
        with self.turtle.jump_stitch(): 
            currpos = list(self.turtle.position())
            #print(currpos)
            self.turtle.goto(currpos[0] + letter_gap*fontsize, currpos[1])
        #print("DRAEW")
        
    def draw_string(self, fontname, string, fontsize, colours='#000000', thicknesses = 1, fills=True, outlines=False, letter_gaps=None, turtle=None, flip_y=False):  # TODO make a version that considers kerning 

        # this draws a multiline string, automatically drawing letter gaps as desired 
        # if fills is True, will fill the text with satin stitch. else, will draw the text outline 

        if turtle is None: 
            if self.turtle is None: 
                raise ValueError("MUST DECLARE turtle TO USE IN LetterDrawer.draw_one_letter in either draw_one_letter() or LetterDrawer() init") 
            turtle = self.turtle 

        startx, starty = turtle.position() 

        #print("DRAWING STRING", string)

        if isinstance(colours, list): 
            assert len(colours) >= len(string), "'colours' in LetterDrawer.draw_string is a list; it's length must be at least length of the string! (characters like '\\n' and ' ' will not use the colour, but will still have an item on the colours list assigned to them)" 

        if isinstance(thicknesses, list): 
            assert len(thicknesses) >= len(string), "'thicknesses' in LetterDrawer.draw_string is a list; it's length must be at least length of the string! (characters like '\\n' and ' ' will not use the colour, but will still have an item on the colours list assigned to them)" 

        if isinstance(fills, list): 
            assert len(fills) >= len(string), "'fills' in LetterDrawer.draw_string is a list; it's length must be at least length of the string! (characters like '\\n' and ' ' will not consider the fill variable, but will still have an item on the fills list assigned to them)" 

        if isinstance(outlines, list): 
            assert len(outlines) >= len(string), "'outlines' in LetterDrawer.draw_string is a list; it's length must be at least length of the string! (characters like '\\n' and ' ' will not consider the outline variable, but will still have an item on theoutlines list assigned to them)" 

        if isinstance(letter_gaps, list): 
            assert len(letter_gaps) >= len(string)-1, "'letter_gaps' in LetterDrawer.draw_string is a list; it's length must be at least (length of the string - 1)! (characters like '\\n' and ' ' will not consider the outline variable, but will still have an item on theoutlines list assigned to them)" 


        #print("HELLO>..")

        for cidx in range(len(string)-1): 
            if string[cidx] in ['\n', '\r']: 
                # newline 
                with turtle.jump_stitch(): 
                    starty -= fontsize*LetterDrawer.line_spacing
                    turtle.goto(startx, starty) 
                continue 
            if isinstance(colours, str): 
                col = colours 
            else: 
                col = colours[cidx] 
            
            if isinstance(thicknesses, int): 
                thickness = thicknesses 
            else: 
                thickness = thicknesses[cidx] 

            if isinstance(fills, bool): 
                fill = fills 
            else: 
                fill = fills[cidx] 
                
            if isinstance(outlines, bool): 
                outline = outlines 
            else: 
                outline = outlines[cidx] 
                
            #print("DRAWING LETTER", string[cidx], "FILL", fill)
            self.draw_one_letter(fontname, LetterDrawer.char_to_name(string[cidx]), fontsize, col, thickness, fill, outline, turtle, flip_y) 

            if isinstance(letter_gaps, list): 
                letter_gap = letter_gaps[cidx] 
            else: 
                letter_gap = letter_gaps 
            self.draw_letter_gap(fontsize, letter_gap) 
        
        cidx = len(string) - 1 
        # draw last letter 
        if string[cidx] in ['\n', '\r']: 
            # newline 
            with turtle.jump_stitch(): 
                starty -= fontsize*LetterDrawer.line_spacing
                turtle.goto(startx, starty) 
        else: 
            if isinstance(colours, str): 
                col = colours 
            else: 
                col = colours[cidx] 
            
            if isinstance(thicknesses, int): 
                thickness = thicknesses 
            else: 
                thickness = thicknesses[cidx] 

            if isinstance(fills, bool): 
                fill = fills 
            else: 
                fill = fills[cidx] 
                
            if isinstance(outlines, bool): 
                outline = outlines 
            else: 
                outline = outlines[cidx] 
                
            #print("DRAWING LETTER", string[-1], "FILL", fill)
            self.draw_one_letter(fontname, LetterDrawer.char_to_name(string[cidx]), fontsize, col, thickness, fill, outline, turtle, flip_y) 

            if isinstance(letter_gaps, list) and len(letter_gaps) > cidx: # if we have another letter gap, include it. 
                letter_gap = letter_gaps[cidx] 
                self.draw_letter_gap(fontsize, letter_gap) 
        

    punctuation_to_name = {'!': 'exclam', 
                           '@': 'at', 
                           '#': 'numbersign', 
                           '$': 'dollar', 
                           '%': 'percent', 
                           '^': 'circumflex', 
                           '&': 'ampersand', 
                           '*': 'asterisk', 
                           '(': 'parenleft', 
                           ')': 'parenright', 
                           '{': 'braceleft', 
                           '}': 'braceright', 
                           '.': 'period', 
                           ',': 'comma', 
                           '"': "quotedbl", 
                           "'": 'quotesingle', 
                           '?': 'question', 
                           '<': 'guilsinglleft', 
                           '>': 'guilsinglright', 
                           '[': 'bracketleft', 
                           ']': 'bracketright', 
                           '_': 'underscore', 
                           '-': 'hyphen', 
                           ':': 'colon', 
                           ';': 'semicolon', 
                           '/': 'slash', 
                           '\\': 'backslash', 
                           '+': 'plus', 
                           '=': 'equal', 
                           '|': 'bar', 
                           '~': 'tilde', 
                           '`': 'quotereversed', 
                           '©': 'copyright', 
                           }

    @classmethod 
    def char_to_name(cls, char:str): 
        # converts a 1-length string (character) to its identifier (in the unpacked .otf/.ttf svgs)
        if char == ' ': 
            return 'space' 
        if char.isdigit(): 
            digit_to_name = {'0': 'zero', 
                                '1': 'one', 
                                '2': 'two', 
                                '3': 'three', 
                                '4': 'four', 
                                '5': 'five', 
                                '6': 'six', 
                                '7': 'seven', 
                                '8': 'eight', 
                                '9': 'nine', }
            return digit_to_name[char] 
        
        if char.isalpha(): 
            return char # normal character 
        
        try: 
            return LetterDrawer.punctuation_to_name[char] 
        except: 
            raise ValueError("CANNOT RECOGNIZE CHARACTER '{}'".format(char)) 


    def clear_fonts(self): 
        # clears loaded fonts, freeing up memory 
        for td in self.created_tmpdirs: 
            del td 
        self.created_tmpdirs = [] 
        self.loaded_fonts = {} 


