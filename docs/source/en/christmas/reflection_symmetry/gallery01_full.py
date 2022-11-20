from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(20):
    for side in range(6):
        for direction in [1, -1]:
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

        needle.right(60)

needle.visualise()