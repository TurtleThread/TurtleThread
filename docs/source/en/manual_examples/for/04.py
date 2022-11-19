from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(25):
    for ray in range(8):
        needle.forward(100)
        needle.backward(100)
        needle.right(45)
        print(ray)

needle.visualise()