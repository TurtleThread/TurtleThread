import random
from turtlethread import Turtle

needle = Turtle()

with needle.running_stitch(30):

    # Draw the star in the top of the christmas tree
    needle.right(360 / 5*2)
    for p in range(5):
        needle.forward(30)
        needle.right(150)
        needle.forward(30)
        needle.left(150)
        needle.right(360/5)
    
    # Reset back to start
    needle.home()

    # Draw christmas tree with ornaments
    retning = 1
    for gren_nummer in range(1, 10):
        retning *= -1  # Turn around for each branch
        y = 30 * gren_nummer
        x = 10 * gren_nummer
        
        # Add some randomness with regards to where the branch ends up
        jitter_x = random.randint(-x//3, x//3)
        jitter_y = random.randint(-10, 10)

        # Go to where the branch ends
        needle.goto(retning * x + jitter_x, y + jitter_y)

        # Draw ornament
        radius = random.randint(10, 20)
        needle.circle(-radius)

needle.visualise()