"""
Hilbert curve
=============

"""

from turtlethread import Turtle


def tegn_hilbertkurve(needle, step_length, recursion_level, angle=90):
    if recursion_level == 0:
        return

    needle.right(angle)
    tegn_hilbertkurve(needle, step_length, recursion_level-1, -angle)

    needle.forward(step_length)
    needle.left(angle)
    tegn_hilbertkurve(needle, step_length, recursion_level-1, angle)

    needle.forward(step_length)
    tegn_hilbertkurve(needle, step_length, recursion_level-1, angle)

    needle.left(angle)
    needle.forward(step_length)
    tegn_hilbertkurve(needle, step_length, recursion_level-1, -angle)
    needle.right(angle)


needle = Turtle()

with needle.running_stitch(20):
    tegn_hilbertkurve(needle, 20, 4)

needle.save("hilbert.jef")
needle.save("hilbert.png")