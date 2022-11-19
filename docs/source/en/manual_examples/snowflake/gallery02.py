from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(10):
    needle.forward(40*2)
    needle.left(90)
    needle.forward(30*2)
    needle.left(127)
    needle.forward(50*2)
    needle.right(127)
    needle.right(90)
    
    needle.left(60)
    
needle.visualise()