from turtlethread import Turtle

def tegn_arm(nål, lengde):
    # Gå litt frem
    tegn_arm(nål, 0.4*lengde)

    # Tegn første "gren", denne peker litt nedover
    nål.right(45)
    tegn_arm(nål, lengde*0.3)
    nål.backward(lengde*0.3)
    nål.left(45)
    # Tegn andre "gren", denne peker litt oppover
    nål.left(45)
    tegn_arm(nål, lengde*0.3)
    nål.backward(lengde*0.3)
    nål.right(45)

    # Gå litt fremover
    tegn_arm(nål, lengde*0.6)

nål = Turtle()
with nål.running_stitch(30):
    tegn_arm(nål, 200)

nål.visualise()