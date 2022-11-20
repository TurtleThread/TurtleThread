from turtlethread import Turtle

def draw_arm(needle, length, rekursion_level):
    if rekursion_level == 0:
        needle.forward(length)
    else:
        # Move forward a little bit
        needle.forward(length)

        # Draw the first "branch" pointing a little downwards
        needle.right(30)
        draw_arm(needle, 0.75*length, rekursion_level-1)
        needle.backward(0.75*length)
        needle.left(30)
        # Draw the second "branch" pointing a little upwards
        needle.left(30)
        draw_arm(needle, 0.75*length, rekursion_level-1)
        needle.backward(0.75*length)
        needle.right(30)

needle = Turtle()
with needle.running_stitch(30):
    needle.left(90)
    draw_arm(needle, 50, 3)
needle.visualise()