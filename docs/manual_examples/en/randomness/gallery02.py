from turtlethread import Turtle
import random

needle = Turtle()

with needle.running_stitch(20):
    needle.circle(10)
    for sirkel in range(5):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        needle.goto(x, y)
        radius = random.randint(5, 40)
        needle.circle(radius)

needle.visualise()