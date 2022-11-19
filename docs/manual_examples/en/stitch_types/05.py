from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(30):
    needle.forward(60)

needle.visualise()
needle.save("pattern_running_stitch_30.txt")