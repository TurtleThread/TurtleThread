from turtlethread import Turtle

needle = Turtle()
# Create 2 stitches with 30 steps between 
with needle.running_stitch(30):
    needle.forward(60)
    
# Jump 45 steps forwards without creating any stitches. 
# (If the machine supports it, the thread is trimmed.)
with needle.jump_stitch():
    needle.forward(45)

# Create 2 stitches with 30 steps between 
with needle.running_stitch(30):
    needle.forward(60)

needle.visualise()
needle.save("pattern_jump.txt")