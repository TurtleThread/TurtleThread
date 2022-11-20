import turtlethread

needle = turtlethread.Turtle()
with needle.running_stitch(30):

    for arm in range(6):
        for direction in [-1, 1]:
            # Move forward a little bit
            needle.forward(90)

            # Draw the "branch", which will point either downards or upwards, depending on the direction
            needle.right(30*direction)
            needle.forward(60)
            needle.backward(60)
            needle.right(-30*direction)
        
            # Move a bit forward and then back to start
            needle.forward(90)
            needle.backward(180)

        # Rotate 60 degrees to the right to draw six branches
        needle.right(60)

needle.visualise()
