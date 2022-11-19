import random
from turtlethread import Turtle

nål = Turtle()

antall_stjerner = random.randint(1, 10)
for stjerne in range(antall_stjerner):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    with nål.jump_stitch():
        nål.goto(x, y)

    with nål.running_stitch(25):
        antall_stråler = random.randint(3, 10)
        for stråle in range(antall_stråler):
            strålelengde = random.randint(25, 100)
            nål.forward(strålelengde)
            nål.backward(strålelengde)
            nål.right(360 / antall_stråler)

nål.visualise()
