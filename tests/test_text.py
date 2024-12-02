
# to import turtlethread 
import sys 
sys.path.insert(1, "./../src")

import turtlethread 


test_str = 'TEXT SAMPLE\n\na'
'''SAMPLE 

© Bernina (Singapore) 
Pte. Ltd. '''


if __name__ == '__main__': 
    print("STARTED")
    with turtlethread.LetterDrawer(turtlethread.Turtle(scale=0.75)) as ld: 

        with ld.turtle.jump_stitch(): 
            ld.turtle.goto(-350, 300)
        
        #print(ld.turtle.position())
        ld.load_font('Arial') # outputs the location of the font file used 
        ld.load_font('Calibri')
        ld.load_font('Comic') # comic sans 
        ld.load_font('Times') # times new roman 

        # multi-font text part 
        #print("HEF:OIDN")
        ld.draw_one_letter('Arial', 'T', 120, fill=False, outline=True) 
        ld.draw_letter_gap(120) 
        #print("DREW A LETTER")
        ld.draw_one_letter('Calibri', 'E', 120, fill=False, outline=True) 
        ld.draw_letter_gap(120) 
        ld.draw_one_letter('Comic', 'X', 120, fill=False, outline=True) 
        ld.draw_letter_gap(120) 
        ld.draw_one_letter('Times', 'T', 120, fill=False, outline=True) 
        ld.draw_letter_gap(120) 

        
        ld.draw_string('Arial', "SAMPLE", 120, fills=False, outlines=True) 
        
        with ld.turtle.jump_stitch(): 
            ld.turtle.goto(-350, 300)
        
        ld.draw_string('Arial', "\n\nabcqz", 120, fills=False, outlines=True)

        # flip y axis 
        '''from turtlethread.base_turtle import Vec2D 
        for sg in ld.turtle.pattern.stitch_groups: 
            for pidx in range(len(sg._positions)): 
                sg._positions[pidx] = Vec2D(sg._positions[pidx][0], -sg._positions[pidx][1]) '''

        # save 
        from pathlib import Path
        savedir = Path(__file__).parent / "visualise_postscript" 
        eps_path = savedir / "test_text.eps" 
        png_path = savedir / "test_text.png" 

        ld.turtle.save(str(savedir / "test_text.exp"))
        

        # visualize 
        import turtle 
        #turtle.screensize(5000, 5000)
        ld.turtle.visualise(done=False, bye=False, clean=True, width=2000, height=2000)


        turtle.Screen().getcanvas().postscript(file=eps_path)
        
        # get png version - requires Ghostscript, https://stackoverflow.com/questions/44587376/oserror-unable-to-locate-ghostscript-on-paths 
        from PIL import Image 
        img = Image.open(eps_path) 
        img.save(png_path, 'png') 

    
    # NOTE: if not using as context manager, should call clear_fonts after loading them. 
    '''Example: 
    ld = turtlethread.LetterDrawer(turtlethread.Turtle()) 
    ld.load_font('Arial', './turtlethread/fonts/Arial.ttf') 
    ld.draw_string('Arial', test_str, 100) # only supports drawing one line for now 
    ld.turtle.visualise(done=False, bye=False)
    ld.clear_fonts() 
    del ld 
    '''
