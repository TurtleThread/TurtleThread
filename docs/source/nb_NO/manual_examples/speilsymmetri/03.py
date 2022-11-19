import turtlethread

nål = turtlethread.Turtle()
with nål.running_stitch(30):

    for arm in range(6):
        for retning in [-1, 1]:
            # Gå litt frem
            nål.forward(90)

            # Tegn første "gren", denne peker enten litt nedover eller litt oppover, avhengig av retning
            nål.right(30*retning)
            nål.forward(60)
            nål.backward(60)
            nål.right(-30*retning)
        
            # Gå litt frem og tilbake
            nål.forward(90)
            nål.backward(180)

        # Roter 60 grader mot høyre for å tegne seks grener
        nål.right(60)

nål.visualise()