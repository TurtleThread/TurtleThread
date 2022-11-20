from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    for stråle in range(8):
        nål.forward(100)
    nål.backward(100)
    nål.right(45)
    print(stråle)

nål.visualise()