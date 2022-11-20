"""
Hilbert curve
=============

.. figure:: /../../_static/figures/auto_examples/hilbert/hilbert.jpg
     :width: 100%
     :alt: An image of the embroidery machine making the Hilbert curve.


"""

from turtlethread import Turtle


def draw_hilbertkurve(needle, step_length, recursion_level, angle=90):
    if recursion_level == 0:
        return

    needle.right(angle)
    draw_hilbertkurve(needle, step_length, recursion_level-1, -angle)

    needle.forward(step_length)
    needle.left(angle)
    draw_hilbertkurve(needle, step_length, recursion_level-1, angle)

    needle.forward(step_length)
    draw_hilbertkurve(needle, step_length, recursion_level-1, angle)

    needle.left(angle)
    needle.forward(step_length)
    draw_hilbertkurve(needle, step_length, recursion_level-1, -angle)
    needle.right(angle)


needle = Turtle()

with needle.running_stitch(20):
    draw_hilbertkurve(needle, 20, 5)

needle.save("hilbert.jef")
needle.save("hilbert.png")
