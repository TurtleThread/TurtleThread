from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    for stråle in range(6):
        nål.forward(100)
        nål.backward(100)
        nål.right(60)

nål.visualise()