"""
Brodere en beskjed med morsekode
================================

I dette eksempelet skal vi se på hvordan vi kan oversette beskjeder til morsekode
og hvordan vi kan lage et broderimønster fra disse beskjedene.
"""

from turtlethread import Turtle


def tegn(pen, steg, hoyde, lengde):
  pen.left(90)
  pen.forward(hoyde)
  pen.right(90)
  pen.forward(steg*lengde)
  pen.right(90)
  pen.forward(hoyde)
  pen.left(90)
 

def strek(pen, steg, hoyde):
  tegn(pen, steg, hoyde, 3)

 
def prikk(pen, steg, hoyde):
  tegn(pen, steg, hoyde, 1)
 
 
def tegn_morse_tegn(tegn, pen, steg, hoyde):
  if tegn == ".":
    prikk(pen, steg, hoyde)
  elif tegn == "-":
    strek(pen, steg, hoyde)
  elif tegn == " ":
    pen.forward(steg)


 
def tegn_morsekode(morsekode, pen, steg=10, hoyde=50):
  pen.forward(steg/2)
  for morsebokstav in morsekode:
    tegn_morse_tegn(morsebokstav, pen, steg=steg, hoyde=hoyde)
    pen.forward(steg)
  pen.forward(steg/2)


MORSEALFABET = {
  'A':'.-',
  'B':'-...',
  'C':'-.-.', 'D':'-..', 'E':'.',
  'F':'..-.', 'G':'--.', 'H':'....',
  'I':'..', 'J':'.---', 'K':'-.-',
  'L':'.-..', 'M':'--', 'N':'-.',
  'O':'---', 'P':'.--.', 'Q':'--.-',
  'R':'.-.', 'S':'...', 'T':'-',
  'U':'..-', 'V':'...-', 'W':'.--',
  'X':'-..-', 'Y':'-.--', 'Z':'--..',
  'Æ':'.-.-', 'Ø':'---.', 'Å': '.--.-',
  '1':'.----', '2':'..---', '3':'...--',
  '4':'....-', '5':'.....', '6':'-....',
  '7':'--...', '8':'---..', '9':'----.',
  '0':'-----', ', ':'--..--', '.':'.-.-.-',
  '?':'..--..', '/':'-..-.', '-':'-....-',
  '(':'-.--.', ')':'-.--.-', ' ': '  '
}

def oversett_tekst_til_morse(tekst):
  morsetekst = ""
  for bokstav in tekst:
    morsetekst += MORSEALFABET[bokstav.upper()]
    morsetekst += " "
  return morsetekst
  

def tegn_morsekode_fra_tekst(tekst, pen, steg=10, hoyde=50):
  morsekode = oversett_tekst_til_morse(tekst)
  tegn_morsekode(morsekode, pen, steg=steg, hoyde=hoyde)
  

penn = Turtle()
with penn.running_stitch(20):
    tegn_morsekode_fra_tekst("Hello world", penn, 40, 200)

penn.save("morse.dst")
penn.save("morse.jef")

penn = Turtle()
with penn.running_stitch(20):
    tegn_morsekode_fra_tekst("Hei verden", penn, 40, 200)

penn.save("no_morse.dst")
penn.save("no_morse.jef")
penn.save("no_morse.png")
