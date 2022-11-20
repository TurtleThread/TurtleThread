from turtlethread import Turtle

nål = Turtle()

antall_kronblader = 8
with nål.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            nål.forward(300)
            nål.right(90)
        nål.right(360 / antall_kronblader)

nål.visualise()
nål.save("blomst.png")
nål.save("blomst.svg")
nål.save("blomst.dst")