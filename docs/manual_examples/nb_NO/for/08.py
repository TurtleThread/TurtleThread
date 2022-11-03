from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    for stråle in range(50, 250, 25):
        nål.forward(stråle)
        nål.backward(stråle)
        nål.right(45)
        print(stråle)

nål.visualise()
