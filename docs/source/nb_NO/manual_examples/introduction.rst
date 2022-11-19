Ditt første skilpaddebroderi
============================

Nå skal vi lage vårt første skilpaddebroderi.
Det første vi må gjøre er å importere TurtleThread (pass på at det er `installert <../installation.html>`_).

.. include-turtlethread:: introduction/01.py
    :linenos:
    :lines: 1

Så oppretter vi et skilpaddeobjekt som vi skal bruke for å tegne med

.. include-turtlethread:: introduction/01.py
    :linenos:
    :lines: 1-3
    :emphasize-lines: 3

Nå har vi alt vi trenger for å begynne å lage mønster. La oss begynne med en strek.
For å tegne en strek bruker vi ``forward`` og bestemmer hvor langt vi vil gå (f.eks 300 steg). 

.. include-turtlethread:: introduction/01.py
    :linenos:
    :emphasize-lines: 4

Denne koden flytter skilpadden 300 steg, men den lager ingen søm. 
For at skilpadden skal sy mens den flytter seg må vi bruke forward kommandoen inne i en søm-blokk.


Få skilpadda til å brodere mens den går
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Den enkleste søm-blokken er en som heter ``running_stitch`` (Se :ref:`stitch-types` for mer detaljer). I en running stitch-block så broderer vi
en rett strek med et fast mellomrom mellom hvert sting.

.. include-turtlethread:: introduction/02.py
    :linenos:
    :lines: 1-5
    :emphasize-lines: 4

Her har vi lagd kode som flytter skilpadda 300 steg fremover, med en running stitch søm, hvor vi
setter et sting for hvert trettiende steg. Dette tilsvarer at vi setter ca et sting per tredje millimeter.
La oss se på hvordan dette ser ut. For å gjøre det kan vi bruke ``visualise``-funksjonen, som bruker
det innebygde ``turtle``-biblioteket for å tegne broderiet vårt.


.. include-turtlethread:: introduction/02.py
    :linenos:
    :emphasize-lines: 6

.. image:: introduction/manual_code_output/02.svg
  :width: 180
  :alt: En rett linje med korte vertikale linjer på tvers som indikerer hvor stingene plasseres.
  :class: sphx-glr-script-out

Nå har vi en søm som gir en rett strek fremover.
For å skifte retning kan vi bruke ``right`` og sende inn antall grader vi vil rotere (f.eks 90 grader). 

.. include-turtlethread:: introduction/03.py
    :linenos:
    :emphasize-lines: 6-7

.. image:: introduction/manual_code_output/03.svg
  :width: 180
  :alt: En rett horisontal linje etterfulgt av en vertikal linje nedover med samme lengde. Begge linjene har korte vertikale linjer på tvers som indikerer hvor stingene plasseres.
  :class: sphx-glr-script-out

Med en for løkke kan vi gjenta dette fire ganger for å få en firkant:

.. include-turtlethread:: introduction/04.py
    :linenos:
    :emphasize-lines: 5-7
    
.. image:: introduction/manual_code_output/04.svg
  :width: 180
  :alt: En firkant med korte vertikale linjer på tvers som indikerer hvor stingene plasseres.
  :class: sphx-glr-script-out

Hvis vi bruker en ny løkke og tegner firkanten åtte ganger, så får vi en fin blomst:

.. include-turtlethread:: introduction/05.py
    :emphasize-lines: 5
    :linenos:

.. image:: introduction/manual_code_output/05.svg
  :width: 180
  :alt: Eight squares placed on top of each other to form what looks like a flower.
  :class: sphx-glr-script-out

Det kan ofte være lurt å finne de variable størrelsene i programmet, og la de være pythonvariabler.
En variabel størrelse i programmet vi akkurat lagde er hvor mange kronblader, så la oss lage en
pythonvariabel som lagrer antallet kronblader

.. include-turtlethread:: introduction/06.py
    :emphasize-lines: 5, 7
    :linenos:
    :lines: 1-13
    
.. image:: introduction/manual_code_output/06.svg
  :width: 180
  :alt: Åtte roterte firkanter plassert opp å hverandre som tilsammen danner en blomst
  :class: sphx-glr-script-out


.. admonition:: Prøv selv:

    * Prøv å endre koden for å endre antall kronblader for å få en blomst slik som den under:

    .. image:: introduction/manual_code_output/07.svg
        :width: 180
        :alt: Ti roterte firkanter plassert opp å hverandre som tilsammen danner en blomst
        :class: sphx-glr-script-out

    .. collapse:: Trykk her for å se hvordan den ferdige koden kan se ut
    
        .. include-turtlethread:: introduction/07.py
            :linenos:
            :lines: 1-13
            :emphasize-lines: 5


Lagre mønsteret
^^^^^^^^^^^^^^^

Nå som vi har et fint motiv kan vi for eksempel lagre det som PNG eller SVG bilder

.. include-turtlethread:: introduction/06.py
    :linenos:
    :lines: 1-15
    :emphasize-lines: 14-15

Under er ``blomst.svg`` fila csom vi nettopp lagde

.. image:: introduction/manual_code_output/blomst.svg
    :width: 180
    :alt: Åtte roterte firkanter plassert opp å hverandre som tilsammen danner en blomst

Eller vi kan lagre DST-fil for å bruke det med en broderimasking

.. include-turtlethread:: introduction/06.py
    :linenos:
    :emphasize-lines: 16

.. image:: ../../../_static/figures/firkantblomst_sydd.png
  :width: 400
  :alt: Eksempelbroderi laget med TurtleThread