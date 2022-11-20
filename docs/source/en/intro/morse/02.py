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
        draw_morse_symbol(morsebokstav, needle, length=length, height=height)
        needle.forward(length)  # We add a unit-length space between each symbol

    # We want a small space at the end also. This is not necessary, but makes the embroidery prettier.
    needle.forward(length/2)

MORSE_ALPHABET = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   '1': '.----',
    '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',  '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '   '
}
