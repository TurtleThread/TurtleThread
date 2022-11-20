import turtlethread

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    # Move forward a little bit
    needle.forward(90)

    # Draw a "branch" that points a little downwards
    needle.right(45)
    needle.forward(90)

needle.visualise()
