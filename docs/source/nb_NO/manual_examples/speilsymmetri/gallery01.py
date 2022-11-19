from turtlethread import Turtle

nål = Turtle()
retning = 1

grenvinkel = 60
with nål.running_stitch(20):
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

nål.visualise()