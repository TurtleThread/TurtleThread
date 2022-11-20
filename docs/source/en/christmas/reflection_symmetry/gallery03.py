from turtlethread import Turtle

needle = Turtle()
direction = 1

with needle.running_stitch(20):
    for radius in range(24, 11, -4):
        needle.forward(30)
        needle.circle(radius*direction)
    needle.backward(120)

needle.visualise()