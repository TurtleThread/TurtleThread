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

needle = Turtle()
with needle.running_stitch(30):
    tegn_morsekode("... --- ...", needle, 60, 200)

needle.save("sos.svg")
