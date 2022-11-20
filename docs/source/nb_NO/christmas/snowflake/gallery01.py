from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(10):
    # Roter snøflaket en halv runde
    nål.right(30)
    
    # Tegn en av armene til hovedsnøflaket
    nål.forward(100)
    nål.right(90)
    nål.circle(30)
    nål.circle(20)
    nål.circle(10)
    nål.left(90)
    nål.backward(100)
    nål.left(60)
        

    # Roter snøflaket 30 grader før vi tegner det andre snøflaket
    nål.right(30)
    # Tegn armen til det andre snøflaket
    nål.forward(40)
    nål.right(90)
    nål.circle(10)
    nål.left(90)
    nål.backward(40)
    nål.left(60)

nål.visualise()
