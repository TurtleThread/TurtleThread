from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(20):
    needle.forward(60)

needle.visualise()
needle.save("pattern_running_stitch_20.txt")