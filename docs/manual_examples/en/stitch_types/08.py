from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(30):
    needle.forward(60)
needle.right(90)
needle.forward(30)

needle.visualise()