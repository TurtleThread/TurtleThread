import turtlethread

nål = turtlethread.Turtle()
with nål.running_stitch(30):

    for arm in range(6):
        for direction in [-1, 1]:
            # Move forward a little bit
            nål.forward(90)

            # Draw the "branch", which will point either downards or upwards, depending on the direction
            nål.right(30*direction)
            nål.forward(60)
            nål.backward(60)
            nål.right(-30*direction)
        
            # Move a bit forward and then back to start
            nål.forward(90)
            nål.backward(180)

        # Rotate 60 degrees to the right to draw six branches
        nål.right(60)

nål.visualise()
