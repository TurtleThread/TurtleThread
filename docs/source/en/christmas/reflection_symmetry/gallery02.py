from turtlethread import Turtle

needle = Turtle()
direction = 1

with needle.running_stitch(20):
    needle.forward(120)
    needle.circle(direction * 50, 220)
    needle.home()

needle.visualise()