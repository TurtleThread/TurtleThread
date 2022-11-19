from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(10):
    # Rotate snowflake half a turn
    needle.right(30)
    
    # Draw arm of main snowflake
    needle.forward(100)
    needle.right(90)
    needle.circle(30)
    needle.circle(20)
    needle.circle(10)
    needle.left(90)
    needle.backward(100)
    needle.left(60)
        

    # Rotate 30 degrees before drawing the arm of the second snowflake
    needle.right(30)
    # Draw arm of second snowflake
    needle.forward(40)
    needle.right(90)
    needle.circle(10)
    needle.left(90)
    needle.backward(40)
    needle.left(60)

needle.visualise()
