.. _morse:

Brodere en beskjed med morsekode
--------------------------------

I dette eksempelet skal vi se på hvordan vi kan oversette beskjeder til morsekode og hvordan vi kan lage et broderimønster fra disse beskjedene.

Tegne morsekode
^^^^^^^^^^^^^^^

Vi starter det hele med å importere ``Turtle`` fra ``turtlethread``.

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 1

Da er neste steg å lage kode som tegner denne morsekode med et skilpaddeobjekt. 
Dette gjør vi ved å definere hvordan vi tegner en prikk og en strek. Det vi vet om morsekode er:

- En prikk varer en tidsenhet
- En strek varer tre tidsenheter
- Mellomrommet mellom hvert tegn er tre tidsenheter
- Mellomrommet mellom hvert ord er syv tidsenheter

Basert på dette kan vi tegne prikker og streker med ``turtlethread``. Det er mange måter vi
kan gjøre det på, men vi har valgt denne:

.. image:: ../../../_static/figures/morse/morse_nb_NO.svg

La oss lage en funksjon for å tegne en prikk, en funksjon for å tegne en strek og en funksjon som tar inn et morsetegn (strek eller mellomrom) og tegner det.

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 4-34

Nå har vi kode som tegner hvert tegn i en morsekode, men vi må også lage kode for å tegne
en hel beskjed. 

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 36-48

La oss prøve ut koden så langt ved å tegne SOS (``... --- ...``) med morsekode.

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 50-54

.. image:: morse/manual_code_output/sos.svg
  :width: 400
  :alt: SOS skrevet med morsekode.
  :class: sphx-glr-script-out

Oversette tekst til morsekode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Neste steg er å lage kode som gjør om tekst til morsekode. For å gjøre det bruker
vi ett oppslagsverk (dictionary) som transformerer bokstaver og tegn til morsekode.

.. include-turtlethread:: morse/02.py
    :linenos:
    :lines: 50-67

Så oppretter vi en funksjon som tar inn en tekststreng og gjør den om til morsekode.

.. include-turtlethread:: morse/03.py
    :linenos:
    :lines: 69-76

Tegne tekst som morsekode
^^^^^^^^^^^^^^^^^^^^^^^^^

Vi ser at vi fikk skrevet ut "Hei på deg" med morsetegn. La oss bruke ``tegn_morsekode`` for å tegne denne teksten.

.. include-turtlethread:: morse/04.py
    :linenos:
    :lines: 76-81

.. image:: morse/manual_code_output/hei_på_deg.svg
    :width: 600
    :alt: Teksten "Hei på deg" med morsetegn
    :class: sphx-glr-script-out

Her har vi en fin liten beskjed. La oss putte dette inn i en funksjon som tar inn en tekststreng
og bruker en skilpadde for å tegne morsekoden som representerer den tekststrengen.

.. include-turtlethread:: morse/05.py
    :linenos:
    :lines: 76-85

.. image:: morse/manual_code_output/hei_verden.svg
    :width: 600
    :alt: Teksten "Hei verden" med morsetegn
    :class: sphx-glr-script-out
