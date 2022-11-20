from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(10):
    for arm in range(6):
        nål.forward(40*2)
        nål.left(90)
        nål.forward(30*2)
        nål.left(127)
        nål.forward(50*2)
        nål.right(127)
        nål.right(90)
        
        nål.left(60)
    
nål.visualise()