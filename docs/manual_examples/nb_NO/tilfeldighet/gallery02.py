from turtlethread import Turtle
import random

nål = Turtle()

with nål.running_stitch(20):
    nål.circle(10)
    for sirkel in range(5):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        nål.goto(x, y)
        radius = random.randint(5, 40)
        nål.circle(radius)

nål.visualise()