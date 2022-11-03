from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(20):
    for arm in range(4):
        for retning in [1, -1]:
            nål.right(arm*90)
            nål.forward(120)
            nål.circle(retning * 50, 220)
            nål.home()

nål.visualise()