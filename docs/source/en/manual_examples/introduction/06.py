from turtlethread import Turtle

needle = Turtle()

num_petals = 8
with needle.running_stitch(30):
    for petal in range(num_petals):
        for side in range(4):
            needle.forward(300)
            needle.right(90)
        needle.right(360 / num_petals)

needle.visualise()
needle.save("flower.png")
needle.save("flower.svg")
needle.save("flower.dst")