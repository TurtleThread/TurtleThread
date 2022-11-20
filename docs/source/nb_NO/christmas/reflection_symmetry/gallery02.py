from turtlethread import Turtle

nål = Turtle()
retning = 1

with nål.running_stitch(20):
    nål.forward(120)
    nål.circle(retning * 50, 220)
    nål.home()

nål.visualise()