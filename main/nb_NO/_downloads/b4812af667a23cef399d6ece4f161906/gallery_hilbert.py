"""
Tegn en hilbertkurve
====================

"""

from turtlethread import Turtle


def tegn_hilbertkurve(nål, steglengde, nivå, vinkel=90):
    if nivå == 0:
        return

    nål.right(vinkel)
    tegn_hilbertkurve(nål, steglengde, nivå-1, -vinkel)

    nål.forward(steglengde)
    nål.left(vinkel)
    tegn_hilbertkurve(nål, steglengde, nivå-1, vinkel)

    nål.forward(steglengde)
    tegn_hilbertkurve(nål, steglengde, nivå-1, vinkel)

    nål.left(vinkel)
    nål.forward(steglengde)
    tegn_hilbertkurve(nål, steglengde, nivå-1, -vinkel)
    nål.right(vinkel)


nål = Turtle()

with nål.running_stitch(10):
    tegn_hilbertkurve(nål, 10, 4)

nål.save("hilbert.jef")
nål.save("hilbert.png")