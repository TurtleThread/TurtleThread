from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(20):
    for side in range(6):
        for direction in [1, -1]:
            for radius in range(24, 11, -4):
                needle.forward(30)
                needle.circle(radius*direction)
            needle.backward(120)
        needle.right(60)

needle.visualise()