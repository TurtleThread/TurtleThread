import random
from turtlethread import Turtle

needle = Turtle()

number_of_stars = random.randint(1, 10)
for star in range(number_of_stars):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    with needle.jump_stitch():
        needle.goto(x, y)

    with needle.running_stitch(25):
        number_of_rays = random.randint(3, 10)
        for ray in range(number_of_rays):
            ray_length = random.randint(25, 100)
            needle.forward(ray_length)
            needle.backward(ray_length)
            needle.right(360 / number_of_rays)

needle.visualise()
