"""
Brodere en beskjed med morsekode
================================

I dette eksempelet skal vi se på hvordan vi kan oversette beskjeder til morsekode
og hvordan vi kan lage et broderimønster fra disse beskjedene.

Vi starter det hele med å importere ``Turtle`` fra ``turtlethread``.
"""

from turtlethread import Turtle

#%%
# Da er neste steg å lage kode som tegner denne morsekode med et skilpaddeobjekt. 
# Dette gjør vi ved å definere hvordan vi tegner en prikk og en strek. Det vi vet om morsekode er:
#
# - En prikk varer en tidsenhet
# - En strek varer tre tidsenheter
# - Mellomrommet mellom hvert tegn er tre tidsenheter
# - Mellomrommet mellom hvert ord er syv tidsenheter
# 
# Basert på dette kan vi tegne prikker og streker med ``turtlethread``. Det er mange måter vi
# kan gjøre det på, men vi har valgt denne:
# 
# .. image:: ../figures/morse/morse.svg
# 
# La oss lage en funksjon for å tegne en prikk, en funksjon for å tegne en strek og en funksjon som tar
# inn et morsetegn (strek eller mellomrom) og tegner det.


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

#%%
# Nå har vi kode som tegner hvert tegn i en morsekode, men vi må også lage kode for å tegne
# en hel beskjed. 
 
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


#%%
# La oss prøve ut koden så langt ved å tegne SOS (... --- ...) med morsekode.
penn = Turtle()
with penn.running_stitch(30):
    tegn_morsekode("... --- ...", penn, 60, 200)

penn.save("sos.png")


# %%
# Neste steg er å lage kode som gjør om tekst til morsekode. For å gjøre det bruker
# vi ett oppslagsverk (dictionary) som transformerer bokstaver og tegn til morsekode.

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

# %%
# Så oppretter vi en funksjon som tar inn en tekststreng og gjør den om til morsekode.

def oversett_tekst_til_morse(tekst):
  morsetekst = ""
  for bokstav in tekst:
    morsetekst += MORSEALFABET[bokstav.upper()]
    morsetekst += " "
  return morsetekst

print(oversett_tekst_til_morse("Hei på deg"))

#%%
# Vi ser at vi fikk skrevet ut "Hei på deg" med morsetegn. La oss bruke ``tegn_morsekode`` for å tegne denne teksten.

morsekode = oversett_tekst_til_morse("Hei på deg")
penn = Turtle()
with penn.running_stitch(30):
    tegn_morsekode(morsekode, penn, 60, 200)

penn.save("morsebeskjed1.png")

#%%
# Her har vi en fin liten beskjed. La oss putte dette inn i en funksjon som tar inn en tekststreng
# og bruker en skilpadde for å tegne morsekoden som representerer den tekststrengen.

def tegn_morsekode_fra_tekst(tekst, penn, lengde, høyde):
  morsekode = oversett_tekst_til_morse(tekst)
  tegn_morsekode(morsekode, penn, lengde, høyde)
  

penn = Turtle()
with penn.running_stitch(30):
    tegn_morsekode_fra_tekst("Hello world", penn, 60, 200)

penn.save("no_morse.jef")
penn.save("no_morse.png")
