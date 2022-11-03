from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(30):
    nål.forward(60)

nål.visualise()
nål.save("pattern_running_stitch_30.txt")