import random
from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(20):
    for side in range(20):
        sidelengde = random.randint(5 * side, 20*side)
        nål.forward(sidelengde)
        vinkel = random.randint(45, 90)
        nål.right(vinkel)

nål.visualise()