from turtlethread import Turtle


def draw_dash(needle, length, height):
    """Use the Turtle object ``needle`` to draw a dash.
    """
    needle.left(90)
    needle.forward(height)
    needle.right(90)
    needle.forward(3*length)
    needle.right(90)
    needle.forward(height)
    needle.left(90)

def draw_dot(needle, length, height):
    """Use the Turtle object ``needle`` to draw a dot.
    """
    needle.left(90)
    needle.forward(height)
    needle.right(90)
    needle.forward(length)
    needle.right(90)
    needle.forward(height)
    needle.left(90)

def draw_morse_symbol(symbol, needle, length, height):
    """Use the Turtle object ``needle`` to draw a morse symbol (dot, dash or pause).
    """
    if symbol == ".":
        draw_dot(needle, length, height)
    elif symbol == "-":
        draw_dash(needle, length, height)
    elif symbol == " ":
        needle.forward(length)

def draw_morse_code(morse_code, needle, length, height):
    """Use the Turtle object ``needle`` to draw morse code
    """
    # We want a small space at the beginning. This is not necessary, but makes the embroidery prettier.
    needle.forward(length/2)

    # We can iterate over each letter in a string
    for morsebokstav in morse_code:
        draw_morse_tegn(morsebokstav, needle, length=length, height=height)
        needle.forward(length)  # We add a unit-length space between each symbol

    # We want a small space at the end also. This is not necessary, but makes the embroidery prettier.
    needle.forward(length/2)

needle = Turtle()
with needle.running_stitch(30):
    draw_morse_code("... --- ...", needle, 60, 200)

needle.save("sos.svg")
