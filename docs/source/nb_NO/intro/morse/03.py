from turtlethread import Turtle


def tegn_strek(penn, lengde, høyde):
    """Bruk skilpaddeobjektet ``penn`` for å tegne en strek.
    """
    penn.left(90)
    penn.forward(høyde)
    penn.right(90)
    penn.forward(3*lengde)
    penn.right(90)
    penn.forward(høyde)
    penn.left(90)

def tegn_prikk(penn, lengde, høyde):
    """Bruk skilpaddeobjektet ``penn`` for å tegne prikk.
    """
    penn.left(90)
    penn.forward(høyde)
    penn.right(90)
    penn.forward(lengde)
    penn.right(90)
    penn.forward(høyde)
    penn.left(90)

def tegn_morse_tegn(tegn, penn, lengde, høyde):
    """Bruk skilpaddeobjektet ``penn`` for å tegne et morsetegn (prikk, strek eller pause).
    """
    if tegn == ".":
        tegn_prikk(penn, lengde, høyde)
    elif tegn == "-":
        tegn_strek(penn, lengde, høyde)
    elif tegn == " ":
        penn.forward(lengde)

def tegn_morsekode(morsekode, penn, lengde, høyde):
    """Bruk en skilpadde for å tegne morsekode
    """
    # Vi vil ha litt mellomrom på starten av strengen, dette er ikke nødvendig, men får det til å se pent ut
    penn.forward(lengde/2)

    # Vi kan iterere over hvert tegn i en tekststreng
    for morsebokstav in morsekode:
        tegn_morse_tegn(morsebokstav, penn, lengde=lengde, høyde=høyde)
        penn.forward(lengde)  # Det er en lengdeenhet mellomrom mellom hvert tegn

    # Vi vil ha litt mellomrom på slutten av strengen, dette er ikke nødvendig, men får det til å se pent ut
    penn.forward(lengde/2)

MORSEALFABET = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   'Æ': '.-.-',
    'Ø': '---.',   'Å': '.--.-',  '1': '.----',
    '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',  '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '   '
}

def oversett_tekst_til_morse(tekst):
    morsetekst = ""
    for bokstav in tekst:
        morsetekst += MORSEALFABET[bokstav.upper()]
        morsetekst += " "
    return morsetekst

print(oversett_tekst_til_morse("Hei på deg"))