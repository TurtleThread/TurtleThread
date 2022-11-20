from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(20):
    for side in range(6):
        for retning in [1, -1]:
            for radius in range(24, 11, -4):
                nål.forward(30)
                nål.circle(radius*retning)
            nål.backward(120)
        nål.right(60)

nål.visualise()