import turtlethread

needle = turtlethread.Turtle()
with needle.running_stitch(30):

    for arm in range(6):
        # Move forward a little bit
        needle.forward(90)

        # Draw the first "branch" pointing a little downwards
        needle.right(30)
        needle.forward(60)
        needle.backward(60)
        needle.right(-30)
    
        # Move forward and then back again
        needle.forward(90)
        needle.backward(90)
    
        # Draw the second "branch" pointing a little upwards
        needle.right(-30)
        needle.forward(60)
        needle.backward(60)
        needle.right(30)

        # Move backwards to the starting point
        needle.backward(90)

        # Rotate 60 degrees to the right to draw six branches
        needle.right(60)

needle.visualise()