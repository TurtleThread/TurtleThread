from turtlethread import Turtle

def tegn_arm(nål, lengde, rekursjonsnivå):
    if rekursjonsnivå == 0:
        nål.forward(lengde)
    else:
        # Gå litt frem
        nål.forward(lengde)

        # Tegn første "gren", denne peker litt nedover
        nål.right(30)
        tegn_arm(nål, 0.75*lengde, rekursjonsnivå-1)
        nål.backward(0.75*lengde)
        nål.left(30)
        # Tegn andre "gren", denne peker litt oppover
        nål.left(30)
        tegn_arm(nål, 0.75*lengde, rekursjonsnivå-1)
        nål.backward(0.75*lengde)
        nål.right(30)

nål = Turtle()
with nål.running_stitch(30):
    nål.left(90)
    tegn_arm(nål, 50, 3)
nål.visualise()