from turtlethread import Turtle

def draw_arm(needle, length):
    # Move forward a little bit
    draw_arm(needle, 0.4*length)

    # Draw the first "branch" pointing a little downwards
    needle.right(45)
    draw_arm(needle, length*0.3)
    needle.backward(length*0.3)
    needle.left(45)
    # Draw the second "branch" pointing a little upwards
    needle.left(45)
    draw_arm(needle, length*0.3)
    needle.backward(length*0.3)
    needle.right(45)

    # Move forward a little bit
    draw_arm(needle, length*0.6)

needle = Turtle()
with needle.running_stitch(30):
    draw_arm(needle, 200)

needle.visualise()