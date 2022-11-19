from turtlethread import Turtle

nål = Turtle()
with nål.running_stitch(20):
    nål.forward(60)

nål.visualise()
nål.save("pattern_running_stitch_20.txt")