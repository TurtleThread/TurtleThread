from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(25):
    for ray in range(6):
        ray_length = 100
        needle.forward(ray_length)
        needle.backward(ray_length)
        needle.right(60)

needle.visualise()
