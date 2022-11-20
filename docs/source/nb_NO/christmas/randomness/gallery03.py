import random
from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(30):
    # Tegn ett snøfnugg med seks sider
    for side in range(6):

        # Bestem hvor mange grener vi ønsker
        antall_grener = random.randint(2, 5)

        # Gi det speilsymmetri
        for retning in [1, -1]:

            nål.forward(30)

            # Legg til en liten gren i starten
            nål.right(120 * retning)
            nål.forward(30)
            nål.backward(30)
            nål.left(120 * retning)

            # Legg til et tilfeldig antall grener hvor hver gren har tilfeldig vinkel og lengde
            for gren in range(antall_grener):
                nål.forward(30)
                grenvinkel = random.randint(50, 70)
                grenlengde = random.randint(20, 30)

                nål.right(grenvinkel * retning)
                nål.forward(grenlengde)
                nål.backward(grenlengde)
                nål.left(grenvinkel * retning)

            nål.forward(10)
            nål.backward(60 + 30*antall_grener)

        nål.right(60)

nål.visualise()