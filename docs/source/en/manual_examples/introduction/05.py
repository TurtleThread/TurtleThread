from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(30):
    for petal in range(8):
        for side in range(4):
            needle.forward(300)
            needle.right(90)
        needle.right(45)

needle.visualise()