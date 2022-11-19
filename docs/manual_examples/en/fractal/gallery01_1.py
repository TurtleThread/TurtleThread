from turtlethread import Turtle


def tegn_side(needle, length, rekursion_level):
    if rekursion_level == 0:
        needle.forward(length)
    else:
        tegn_side(needle, length/3, rekursion_level-1)
        needle.left(60)
        tegn_side(needle, length/3, rekursion_level-1)
        needle.right(120)
        tegn_side(needle, length/3, rekursion_level-1)
        needle.left(60)
        tegn_side(needle, length/3, rekursion_level-1)

needle = Turtle()
with needle.running_stitch(30):
    for side in range(3):
        tegn_side(needle, 200, 1)
        needle.right(120)

needle.visualise()