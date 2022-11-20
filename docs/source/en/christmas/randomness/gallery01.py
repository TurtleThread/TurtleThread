import random
from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(20):
    for side in range(20):
        side_length = random.randint(5 * side, 20*side)
        needle.forward(side_length)
        angle = random.randint(45, 90)
        needle.right(angle)

needle.visualise()