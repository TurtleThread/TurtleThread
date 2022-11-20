from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(20):
    for side in range(6):
        for retning in [1, -1]:
            nål.forward(30)
            nål.right(120 * retning)
            nål.forward(15)
            nål.backward(15)
            nål.left(120 * retning)

            for grenlengde in range(30, 21, -4):
                nål.forward(20)
                nål.right(60 * retning)
                nål.forward(grenlengde)
                nål.backward(grenlengde)
                nål.left(60 * retning)

            nål.forward(10)
            nål.backward(100)

        nål.right(60)

nål.visualise()