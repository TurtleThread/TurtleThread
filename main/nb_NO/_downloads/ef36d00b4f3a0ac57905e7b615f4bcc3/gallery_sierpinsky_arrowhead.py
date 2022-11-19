"""
Tegn en Sierpinsky pilspisskurve
================================

"""
from turtlethread import Turtle


def tegn_sierpinsky_pilspiss(nål, steglengde, nivå, vinkel=60):
    if nivå == 0:
        nål.forward(steglengde)
        return

    tegn_sierpinsky_pilspiss(nål, steglengde, nivå-1, -vinkel)
    nål.left(vinkel)
    tegn_sierpinsky_pilspiss(nål, steglengde, nivå-1, vinkel)
    nål.left(vinkel)
    tegn_sierpinsky_pilspiss(nål, steglengde, nivå-1, -vinkel)


nål = Turtle()

with nål.running_stitch(10):
    tegn_sierpinsky_pilspiss(nål, 10, 5)

nål.save("sierpinsky.jef")
nål.save("sierpinsky.png")
