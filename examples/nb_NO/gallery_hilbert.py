"""
Hilbertkurve
====================

.. figure:: /../../_static/figures/auto_examples/hilbert/hilbert.jpg
    :width: 100%
    :alt: Et bilde av at en broderimaskin som broderer en hilbertkurve.
"""

from turtlethread import Turtle


def tegn_hilbertkurve(nål, steglengde, nivå, vinkel=90):
    if nivå == 0:
        return

    nål.right(vinkel)
    tegn_hilbertkurve(nål, steglengde, nivå - 1, -vinkel)

    nål.forward(steglengde)
    nål.left(vinkel)
    tegn_hilbertkurve(nål, steglengde, nivå - 1, vinkel)

    nål.forward(steglengde)
    tegn_hilbertkurve(nål, steglengde, nivå - 1, vinkel)

    nål.left(vinkel)
    nål.forward(steglengde)
    tegn_hilbertkurve(nål, steglengde, nivå - 1, -vinkel)
    nål.right(vinkel)


nål = Turtle()

with nål.running_stitch(20):
    tegn_hilbertkurve(nål, 20, 5)

nål.save("hilbert.jef")
nål.save("hilbert.png")
