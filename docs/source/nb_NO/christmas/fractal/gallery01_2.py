from turtlethread import Turtle

def tegn_side(nål, lengde, rekursjonsdybde):
    if rekursjonsdybde == 0:
        nål.forward(lengde)
    else:
        tegn_side(nål, lengde/3, rekursjonsdybde-1)
        nål.left(60)
        tegn_side(nål, lengde/3, rekursjonsdybde-1)
        nål.right(120)
        tegn_side(nål, lengde/3, rekursjonsdybde-1)
        nål.left(60)
        tegn_side(nål, lengde/3, rekursjonsdybde-1)

nål = Turtle()
with nål.running_stitch(30):
    for side in range(3):
        tegn_side(nål, 200, 2)
        nål.right(120)

nål.visualise()