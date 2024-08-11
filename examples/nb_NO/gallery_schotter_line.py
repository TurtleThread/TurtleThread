"""
Schotter-inspirert linjekunst
=============================

"""

import random

from turtlethread import Turtle


def sett_tilfeldig_retning(turtle, mean, std):
    turtle.setheading(random.gauss(mean, std))


random.seed(42)
nål = Turtle()

høyde = 100
bredde = 50
steg = 10
with nål.running_stitch(steg):
    for j in range(høyde // 4):
        std = j
        for i in range(bredde):
            sett_tilfeldig_retning(nål, 0, std)
            nål.forward(10)

        for i in range(2):
            sett_tilfeldig_retning(nål, 90, std)
            nål.forward(10)

        for i in range(bredde):
            sett_tilfeldig_retning(nål, 180, std)
            nål.forward(10)

        for i in range(2):
            sett_tilfeldig_retning(nål, 90, std)
            nål.forward(10)


nål.save("stotter_linje.jef")
nål.save("stotter_linje.svg")
