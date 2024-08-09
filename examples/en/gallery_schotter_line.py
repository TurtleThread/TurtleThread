"""
Schotter-inspired line art
==========================

"""

import random

from turtlethread import Turtle


def set_random_heading(turtle, mean, std):
    turtle.setheading(random.gauss(mean, std))


random.seed(42)
needle = Turtle()

height = 100
width = 50
step = 10
with needle.running_stitch(step):
    for j in range(height // 4):
        std = j
        for i in range(width):
            set_random_heading(needle, 0, std)
            needle.forward(10)

        for i in range(2):
            set_random_heading(needle, 90, std)
            needle.forward(10)

        for i in range(width):
            set_random_heading(needle, 180, std)
            needle.forward(10)

        for i in range(2):
            set_random_heading(needle, 90, std)
            needle.forward(10)


needle.save("stotter_line.jef")
needle.save("stotter_line.png")
