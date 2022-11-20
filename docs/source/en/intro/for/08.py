from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(25):
    for ray in range(50, 250, 25):
        needle.forward(ray)
        needle.backward(ray)
        needle.right(45)
        print(ray)

needle.visualise()
