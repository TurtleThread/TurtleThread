from turtlethread import Turtle

nål = Turtle()
retning = 1

with nål.running_stitch(20):
    for radius in range(24, 11, -4):
        nål.forward(30)
        nål.circle(radius*retning)
    nål.backward(120)

nål.visualise()