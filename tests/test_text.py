
# to import turtlethread 
import sys 
sys.path.insert(1, "./../src")

import turtlethread 


test_str = '''TEXT SAMPLE 

© Bernina (Singapore) 
Pte. Ltd. '''


if __name__ == '__main__': 
    with turtlethread.LetterDrawer(turtlethread.Turtle()) as ld: 
        #print(ld.turtle.position())
        ld.load_font('Arial') 
        print("HEY")
        #ld.draw_one_letter('Arial', 'a', 100)
        ld.draw_string('Arial', test_str, 100, fills=True) # only supports drawing one line for now 
        ld.turtle.visualise(done=False, bye=False)

        # save 
        from pathlib import Path
        savepath = (Path(__file__).parent / "visualise_postscript" / "test_text.eps") 
        print("SAVING TO", savepath)
        import turtle 
        turtle.Screen().getcanvas().postscript(file=savepath)
    
    # NOTE: if not using as context manager, should call clear_fonts after loading them. 
    '''Example: 
    ld = turtlethread.LetterDrawer(turtlethread.Turtle()) 
    ld.load_font('Arial', './turtlethread/fonts/Arial.ttf') 
    ld.draw_string('Arial', test_str, 100) # only supports drawing one line for now 
    ld.turtle.visualise(done=False, bye=False)
    ld.clear_fonts() 
    del ld 
    '''
