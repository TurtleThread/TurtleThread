from turtlethread import Turtle

needle = Turtle()
direction = 1

with needle.running_stitch(20):
    needle.forward(30)
    needle.right(120 * direction)
    needle.forward(15)
    needle.backward(15)
    needle.left(120 * direction)

    for branch_length in range(30, 21, -4):
        needle.forward(20)
        needle.right(60 * direction)
        needle.forward(branch_length)
        needle.backward(branch_length)
        needle.left(60 * direction)

    needle.forward(10)
    needle.backward(100)

needle.visualise()