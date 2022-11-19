import turtlethread

nål = turtlethread.Turtle()
with nål.running_stitch(30):

    for arm in range(6):
        # Move forward a little bit
        nål.forward(90)

        # Draw the first "branch" pointing a little downwards
        nål.right(30)
        nål.forward(60)
        nål.backward(60)
        nål.right(-30)
    
        # Move forward and then back again
        nål.forward(90)
        nål.backward(90)
    
        # Draw the second "branch" pointing a little upwards
        nål.right(-30)
        nål.forward(60)
        nål.backward(60)
        nål.right(30)

        # Move backwards to the starting point
        nål.backward(90)

        # Rotate 60 degrees to the right to draw six branches
        nål.right(60)

nål.visualise()