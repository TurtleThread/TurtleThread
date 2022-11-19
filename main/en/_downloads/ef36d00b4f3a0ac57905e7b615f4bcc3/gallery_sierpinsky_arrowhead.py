"""
Sierpinsky arrowhead curve
==========================

"""
from turtlethread import Turtle


def draw_sierpinsky_arrowhead(needle, step_length, recursion_level, angle=60):
    if recursion_level == 0:
        needle.forward(step_length)
        return

    draw_sierpinsky_arrowhead(needle, step_length, recursion_level-1, -angle)
    needle.left(angle)
    draw_sierpinsky_arrowhead(needle, step_length, recursion_level-1, angle)
    needle.left(angle)
    draw_sierpinsky_arrowhead(needle, step_length, recursion_level-1, -angle)


needle = Turtle()

with needle.running_stitch(20):
    draw_sierpinsky_arrowhead(needle, 20, 5)

needle.save("sierpinsky.jef")
needle.save("sierpinsky.png")