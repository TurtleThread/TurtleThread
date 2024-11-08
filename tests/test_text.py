
# to import turtlethread 
import sys 
sys.path.insert(1, "./../src")

import turtlethread 




if __name__ == '__main__': 
    ld = turtlethread.LetterDrawer(turtlethread.Turtle()) 
    #print(ld.turtle.position())
    ld.load_font('OpenDyslexic') 
    ld.draw_one_letter('OpenDyslexic', 'h', 50) 
    ld.draw_letter_gap(50) 
    ld.draw_one_letter('OpenDyslexic', 'i', 50) 

