from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(10):
    for arm in range(6):  # Draw arm of main snowflake
        needle.forward(100)
        needle.right(40)
        needle.forward(40)
        needle.backward(40)
        needle.left(40)
        needle.forward(30)
        needle.right(30)
        needle.forward(20)
        needle.backward(20)
        needle.left(30)
        needle.forward(20)

        needle.backward(20)

        needle.right(-30)
        needle.forward(20)
        needle.backward(20)
        needle.left(-30)

        needle.backward(30)

        needle.right(-40)
        needle.forward(40)
        needle.backward(40)
        needle.left(-40)
        needle.backward(100)
        needle.left(60)

    # Rotate 30 degrees before drawing the arm of the second snowflake
    needle.right(30)

    for arm in range(6):  # Draw arm of second snowflake
        needle.forward(50)

        needle.right(40)
        needle.forward(20)
        needle.backward(20)
        needle.left(40)

        needle.forward(30)
        needle.backward(30)

        needle.left(40)
        needle.forward(20)
        needle.backward(20)
        needle.right(40)

        needle.backward(50)
        needle.left(60)

needle.visualise()
