import random
from turtlethread import Turtle

nål = Turtle()

with nål.running_stitch(30):

    # Tegn stjerna i toppen av juletreet
    nål.right(360 / 5*2)
    for p in range(5):
        nål.forward(30)
        nål.right(150)
        nål.forward(30)
        nål.left(150)
        nål.right(360/5)
    
    # Reset back to start
    nål.home()

    # Tegn treet med julekuler på
    retning = 1
    for gren_nummer in range(1, 10):
        retning *= -1  # Snu nåla hver runde
        y = 30 * gren_nummer
        x = 10 * gren_nummer
        
        # Legg på litt tilfeldighet mtp hvor grena ender
        jitter_x = random.randint(-x//3, x//3)
        jitter_y = random.randint(-10, 10)

        # Gå til der grena ender
        nål.goto(retning * x + jitter_x, y + jitter_y)

        # Tegn julekule
        radius = random.randint(10, 20)
        nål.circle(-radius)

nål.visualise()