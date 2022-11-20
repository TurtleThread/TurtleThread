import random
from turtlethread import Turtle

needle = Turtle()
with needle.running_stitch(25):
    number_of_rays = random.randint(3, 10)
    for ray in range(number_of_rays):
        ray_length = random.uniform(25, 125)
        needle.forward(ray_length)
        needle.backward(ray_length)
        needle.right(360 / number_of_rays)

needle.visualise()
