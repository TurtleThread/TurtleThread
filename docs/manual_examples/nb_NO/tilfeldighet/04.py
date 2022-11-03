import random
from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    antall_stråler = random.randint(3, 10)
    for stråle in range(antall_stråler):
        strålelengde = random.uniform(25, 125)
        nål.forward(strålelengde)
        nål.backward(strålelengde)
        nål.right(360 / antall_stråler)

nål.visualise()
