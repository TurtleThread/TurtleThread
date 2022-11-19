import turtlethread

nål = turtlethread.Turtle()
with nål.running_stitch(30):

    for arm in range(6):
        # Gå litt frem
        nål.forward(90)

        # Tegn første "gren", denne peker litt nedover
        nål.right(30)
        nål.forward(60)
        nål.backward(60)
        nål.left(30)
    
        # Gå litt frem og tilbake
        nål.forward(90)
        nål.backward(90)
    
        # Tegn andre "gren", denne peker litt oppover
        nål.left(30)
        nål.forward(60)

nål.visualise()