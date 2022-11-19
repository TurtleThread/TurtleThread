from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(10):
    for arm in range(6):
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
        
    nål.right(30)
    for arm in range(6):
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