import random
from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(30):
    # Draw snowflake with six sides
    for side in range(6):

        # Decide how many branches we want
        antall_grener = random.randint(2, 5)

        # Give it reflection symmetry
        for direction in [1, -1]:

            needle.forward(30)

            # Add one small branch in the beginning
            needle.right(120 * direction)
            needle.forward(30)
            needle.backward(30)
            needle.left(120 * direction)

            # Add a random number of branches, each having a random angle and length
            for gren in range(antall_grener):
                needle.forward(30)
                branch_angle = random.randint(50, 70)
                branch_length = random.randint(20, 30)

                needle.right(branch_angle * direction)
                needle.forward(branch_length)
                needle.backward(branch_length)
                needle.left(branch_angle * direction)

            needle.forward(30)
            needle.backward(60 + 30*antall_grener)

        needle.right(60)

needle.visualise()