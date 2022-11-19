from turtlethread import Turtle

def tegn_arm(nål, lengde, rekursjonsnivå):
    if rekursjonsnivå == 0:
        nål.forward(lengde)
    elif rekursjonsnivå % 2 == 0:
        # Gå litt frem
        tegn_arm(nål, 0.4*lengde, rekursjonsnivå-1)

        # Tegn første "gren", denne peker litt nedover
        nål.right(45)
        tegn_arm(nål, lengde*0.3, rekursjonsnivå-1)
        nål.backward(lengde*0.3)
        nål.left(45)
        # Tegn andre "gren", denne peker litt oppover
        nål.left(45)
        tegn_arm(nål, lengde*0.3, rekursjonsnivå-1)
        nål.backward(lengde*0.3)
        nål.right(45)

        # Gå litt fremover
        tegn_arm(nål, lengde*0.6, rekursjonsnivå-1)
    else:
        # Gå litt frem
        tegn_arm(nål, 0.4*lengde, rekursjonsnivå-1)

        # Tegn første "gren", denne peker litt nedover
        nål.right(60)
        tegn_arm(nål, lengde*0.2, rekursjonsnivå-1)
        nål.backward(lengde*0.2)
        nål.left(60)
        # Tegn andre "gren", denne peker litt oppover
        nål.left(60)
        tegn_arm(nål, lengde*0.2, rekursjonsnivå-1)
        nål.backward(lengde*0.2)
        nål.right(60)
        
        tegn_arm(nål, 0.2*lengde, rekursjonsnivå-1)

        # Tegn tredje "gren", denne peker litt nedover
        nål.right(60)
        tegn_arm(nål, lengde*0.2, rekursjonsnivå-1)
        nål.backward(lengde*0.2)
        nål.left(60)
        # Tegn fjerde "gren", denne peker litt oppover
        nål.left(60)
        tegn_arm(nål, lengde*0.2, rekursjonsnivå-1)
        nål.backward(lengde*0.2)
        nål.right(60)

        # Gå litt fremover
        tegn_arm(nål, lengde*0.4, rekursjonsnivå-1)

nål = Turtle()
with nål.running_stitch(50):
    for arm in range(6):
        tegn_arm(nål, 400, 3)
        nål.backward(400)
        nål.right(60)

nål.visualise()