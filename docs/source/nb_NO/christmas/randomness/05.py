import random
from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(25):
    antall_stjerner = 4
    for stjerne in range(antall_stjerner):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        nål.goto(x, y)

        antall_stråler = random.randint(3, 10)
        for stråle in range(antall_stråler):
            strålelengde = random.randint(25, 100)
            nål.forward(strålelengde)
            nål.backward(strålelengde)
            nål.right(360 / antall_stråler)

nål.visualise()
