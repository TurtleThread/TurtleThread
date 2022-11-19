from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(20):
    for arm in range(4):
        for direction in [1, -1]:
            needle.right(arm*90)
            needle.forward(120)
            needle.circle(direction * 50, 220)
            needle.home()

needle.visualise()