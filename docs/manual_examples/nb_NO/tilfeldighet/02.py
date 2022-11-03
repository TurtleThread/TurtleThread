from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    for stråle in range(6):
        strålelengde = 100
        nål.forward(strålelengde)
        nål.backward(strålelengde)
        nål.right(60)

nål.visualise()
