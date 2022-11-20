import turtlethread

nål = turtlethread.Turtle()
with nål.running_stitch(30):
    # Gå litt frem
    nål.forward(90)

    # Tegn en "gren", denne peker litt nedover
    nål.right(45)
    nål.forward(90)

nål.visualise()