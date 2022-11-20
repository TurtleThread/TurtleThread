from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(30):
    for side in range(4):
        nål.forward(60)
        nål.right(90)

nål.visualise()