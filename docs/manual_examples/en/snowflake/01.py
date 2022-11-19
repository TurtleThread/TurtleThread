from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(50):
    needle.forward(100)

needle.visualise()
