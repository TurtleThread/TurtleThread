from turtlethread import Turtle


def tegn_strek(needle, lengde, høyde):
    """Bruk skilpaddeobjektet ``needle`` for å tegne en strek.
    """
    needle.left(90)
    needle.forward(høyde)
    needle.right(90)
    needle.forward(3*lengde)
    needle.right(90)
    needle.forward(høyde)
    needle.left(90)

def tegn_prikk(needle, lengde, høyde):
    """Bruk skilpaddeobjektet ``needle`` for å tegne prikk.
    """
    needle.left(90)
    needle.forward(høyde)
    needle.right(90)
    needle.forward(lengde)
    needle.right(90)
    needle.forward(høyde)
    needle.left(90)

def tegn_morse_tegn(tegn, needle, lengde, høyde):
    """Bruk skilpaddeobjektet ``needle`` for å tegne et morsetegn (prikk, strek eller pause).
    """
    if tegn == ".":
        tegn_prikk(needle, lengde, høyde)
    elif tegn == "-":
        tegn_strek(needle, lengde, høyde)
    elif tegn == " ":
        needle.forward(lengde)

def tegn_morsekode(morsekode, needle, lengde, høyde):
    """Bruk en skilpadde for å tegne morsekode
    """
    # Vi vil ha litt mellomrom på starten av strengen, dette er ikke nødvendig, men får det til å se pent ut
    needle.forward(lengde/2)

    # Vi kan iterere over hvert tegn i en tekststreng
    for morsebokstav in morsekode:
        draw_morse_symbol(morsebokstav, needle, lengde=lengde, høyde=høyde)
        needle.forward(lengde)  # Det er en lengdeenhet mellomrom mellom hvert tegn

    # Vi vil ha litt mellomrom på slutten av strengen, dette er ikke nødvendig, men får det til å se pent ut
    needle.forward(lengde/2)

needle = Turtle()
with needle.running_stitch(30):
    tegn_morsekode("... --- ...", needle, 60, 200)

needle.save("sos.svg")
