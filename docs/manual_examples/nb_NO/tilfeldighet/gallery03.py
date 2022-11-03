import random
from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(20):
    for side in range(6):
        antall_grener = random.randint(2, 5)

        for retning in [1, -1]:
            nål.forward(30)

            nål.right(120 * retning)
            nål.forward(15)
            nål.backward(15)
            nål.left(120 * retning)

            for gren in range(antall_grener):
                nål.forward(20)
                grenvinkel = random.randint(50, 70)
                grenlengde = random.randint(20, 30)

                nål.right(grenvinkel * retning)
                nål.forward(grenlengde)
                nål.backward(grenlengde)
                nål.left(grenvinkel * retning)

            nål.forward(10)
            nål.backward(40 + 20*antall_grener)

        nål.right(60)

nål.visualise()