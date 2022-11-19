from turtlethread import Turtle

nål = Turtle()
# Sy først 2 sting med 30 steg mellom hvert sting
with nål.running_stitch(30):
    nål.forward(60)
    
# Hopp 45 steg fremover uten å sy sting. Om maskina støtter det kuttes tråden.
with nål.jump_stitch():
    nål.forward(45)

# Sy så 2 sting med 30 steg mellom hvert sting
with nål.running_stitch(30):
    nål.forward(60)

nål.visualise()
nål.save("pattern_jump.txt")