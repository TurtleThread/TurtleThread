from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    for stråle in range(100, 500, 50):
        nål.forward(stråle)
        nål.backward(stråle)
        nål.right(150)
        print(stråle)

nål.visualise()