from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(25):
    for ray in range(100, 500, 50):
        needle.forward(ray)
        needle.backward(ray)
        needle.right(45)
        print(ray)

needle.visualise()