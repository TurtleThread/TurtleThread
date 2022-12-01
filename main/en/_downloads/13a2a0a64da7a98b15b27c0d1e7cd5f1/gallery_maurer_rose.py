"""
Maurer rose
===========

The Maurer rose is a mathematical pattern that looks like a rose. 
You can read more about this pattern on `the Maurer rose Wikipedia page <https://en.wikipedia.org/wiki/Maurer_rose>`_

"""
from turtlethread import Turtle
from math import pi, sin, cos

needle = Turtle()

n = 5
d = 97
with needle.running_stitch(50):
    for theta in range(361):
        k = theta * d * pi / 180
        r = 300 * sin(n * k)
        x = r * cos(k)
        y = r * sin(k)
        needle.goto(x, y)

needle.save("maurer_rose.svg")