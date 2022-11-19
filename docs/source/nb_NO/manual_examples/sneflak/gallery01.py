from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(10):
    nål.right(30)
    for arm in range(6):
        nål.forward(100)
        nål.right(90)
        nål.circle(30)
        nål.circle(20)
        nål.circle(10)
        nål.left(90)
        nål.backward(100)
        nål.left(60)
        
    nål.right(30)
    for arm in range(6):
        nål.forward(40)
        nål.right(90)
        nål.circle(10)
        nål.left(90)
        nål.backward(40)
        nål.left(60)

nål.visualise()