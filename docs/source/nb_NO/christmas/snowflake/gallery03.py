from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(10):
    # Tegn armen til hovedsnøflaket
    nål.forward(100)
    nål.right(40)
    nål.forward(40)
    nål.backward(40)
    nål.left(40)
    nål.forward(30)
    nål.right(30)
    nål.forward(20)
    nål.backward(20)
    nål.left(30)
    nål.forward(20)

    nål.backward(20)

    nål.right(-30)
    nål.forward(20)
    nål.backward(20)
    nål.left(-30)

    nål.backward(30)

    nål.right(-40)
    nål.forward(40)
    nål.backward(40)
    nål.left(-40)
    nål.backward(100)
    nål.left(60)

    # Roter 30 grader før det andre snøflaket tegnes
    nål.right(30)

    # Tegn armen til det andre snøflaket
    nål.forward(50)

    nål.right(40)
    nål.forward(20)
    nål.backward(20)
    nål.left(40)

    nål.forward(30)
    nål.backward(30)

    nål.left(40)
    nål.forward(20)
    nål.backward(20)
    nål.right(40)

    nål.backward(50)
    nål.left(60)

nål.visualise()
