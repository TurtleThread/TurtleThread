from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(30):
    needle.forward(300)
needle.visualise()