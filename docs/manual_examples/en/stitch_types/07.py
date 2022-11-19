from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(30):
    for side in range(4):
        needle.forward(60)
        needle.right(90)

needle.visualise()