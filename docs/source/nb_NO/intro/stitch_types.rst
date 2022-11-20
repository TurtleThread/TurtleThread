.. _stitch-types:

Oversikt over sømmetyper i TurtleThread
---------------------------------------

TurtleThread støtter for øyeblikket to sømmetyper: rettsøm og hoppesøm (sikksakksøm er under utvikling).
I denne guiden skal vi se på hva en sømmetype gjør og hva forskjellen på disse to sømmetypene er. 

Ingen søm
^^^^^^^^^

La oss starte med å opprette en skilpadde som skal styre nåla vår og be den gå 60 steg fremover. 

.. include-turtlethread:: stitch_types/01.py
    :linenos:

Hva skjer hvis vi visualiserer dette?

.. include-turtlethread:: stitch_types/02.py
    :linenos:
    :emphasize-lines: 5

.. image:: stitch_types/manual_code_output/02.svg
  :width: 10
  :alt: Resultat fra koden over.
    Et bilde med kun en trekant som markerer hvor nåla er.
  :class: sphx-glr-script-out

Her ser vi kun markøren for nåla!
Grunnen til det er at vi kun har bedt skilpadden gå fremover, vi har ikke bedt den om å sy med en søm.
Vi kan se dette enda tydeligere hvis vi lagrer broderimønsteret som tekstfil og ser på innholdet i fila. 

.. include-turtlethread:: stitch_types/03.py
    :linenos:

.. literalinclude:: stitch_types/manual_code_output/pattern_no_stitch.txt

Her ser vi at broderimønsteret vårt ikke inneholder noen sting!

Rettsøm
^^^^^^^
For å få skilpadden til å sy mens den beveger seg kan vi bruke en konteksthåndterer som bestemmer sømtype.
Hvis vi for eksempel ønsker rettsøm (running stitch på engelsk) kan vi skrive

.. include-turtlethread:: stitch_types/04.py
    :linenos:
    :emphasize-lines: 4

.. image:: stitch_types/manual_code_output/04.svg
  :width: 100
  :alt: Resultat fra koden over.
    En horisontal blå strek med fire korte vertikale streker med lik avstand mellom hver strek.
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_running_stitch_20.txt

I visualiseringen har det nå dukket opp noen små linjer på tvers som indikerer hvor stingene skal plasseres.
Vi ser at det er sting på posisjonene (0, 0), (20, 0), (40, 0) og (60, 0) altså med 20 steg mellom hvert sting.
Grunnen til at det er akkurat 20 steg mellom hvert sting er at vi bestemte det på linje 4 ved å skrive ``with nål.running_stitch(20)``.
Hvis vi ønsker at stingene skal være 30 steg lange kan vi isteden skrive:

.. include-turtlethread:: stitch_types/05.py
    :linenos:
    :emphasize-lines: 4

.. image:: stitch_types/manual_code_output/05.svg
  :width: 100
  :alt: Resultat fra koden over.
    En horisontal blå strek med tre korte vertikale streker, en i hver ende og en på midten.
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_running_stitch_30.txt

Innrykk er viktig
^^^^^^^^^^^^^^^^^

Legg merke til at line 5 ligger et innrykknivå inn.
Innrykknivå er det Python bruker for å gruppere linjer med kode sammen til en blokk.
Hvis vi legger til nye linjer på samme innrykknivå vil de høre til i samme blokk, altså rettsømblokken, og de vil også utføres med rettsøm:

.. include-turtlethread:: stitch_types/06.py
    :linenos:
    :emphasize-lines: 6-7

.. image:: stitch_types/manual_code_output/06.svg
  :width: 100
  :alt: Resultat fra koden over.
    En horisontal blå strek etterfulgt av en vertikal strek nedover som er halvparten så stor som den horisontale streken.
    Hver strek har små tverrstreker som markerer hvor stingene skal være.
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_angle.txt

Her ser vi at linje 5-7 hører sammen i en blokk som hører under rettsøm konteksten.
Vi kan fortsette å legge så mange linjer vi vil innenfor samme innrykksnivå og de vil bli utført med rettsøm.
Her er et eksempel hvor vi har en for løkke innenfor rettsømkonteksten:

.. include-turtlethread:: stitch_types/07.py
    :linenos:
    :emphasize-lines: 5-7

.. image:: stitch_types/manual_code_output/07.svg
  :width: 100
  :alt: Resultat fra koden over.
    En blå firkant med korte tverrstreker som markerer sting.
  :class: sphx-glr-script-out

Hvis vi derimot legger til en linje på et innrykksnivå utenfor vil den ikke bli utført med rettsøm

.. include-turtlethread:: stitch_types/08.py
    :linenos:
    :emphasize-lines: 6-7

.. image:: stitch_types/manual_code_output/08.svg
  :width: 100
  :alt: Resultat fra koden over.
    En horisontal blå strek med tre korte vertikale streker, en i hver ende og en på midten.
  :class: sphx-glr-script-out

Hoppesøm
^^^^^^^^

Hvis vi ønsker å flytte nåla uten å lage sting kan vi bruke hoppesøm (også kjent som forbindende sting, eller jump stitch på engelsk).
Koden under viser hvordan vi kan bruke hoppesøm til å tegne to streker med et mellomrom mellom


.. include-turtlethread:: stitch_types/09.py
    :linenos:
    :emphasize-lines: 8-10

.. image:: stitch_types/manual_code_output/09.svg
  :width: 100
  :alt: Resultat fra koden over.
    En horisontal blå strek med tre korte vertikale streker, en i hver ende og en på midten, etterfulgt av ett sort kryss som indikerer at tråden skal kuttes, en rød strek som ender i en rød sirkel, som indikerer at nåla skal flyttes dit uten å sy og til slutt en ny horisontal blå strek med tre korte vertikale streker.
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_jump.txt
  :emphasize-lines: 4-5

I visualiseringen ser vi at den første blå linja slutter med et sort kryss.
Hvis broderimaskinen du skal bruke til å utføre instruksjonene støtter det vil tråden bli kuttet her, men ikke alle maskiner støtter dette.
Hvis maskinen din ikke støtter å kutte tråden, må du gjøre det manuelt til slutt. 
I mønsterfila ser vi kommandoene ``TRIM`` på linje 4, som indikerer at tråden skal kuttes her, og ``JUMP`` på linje 5 som indikerer at nåla skal flyttes hit uten å sy. 

Hva er en konteksthåndterer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Som vi nevnte på starten er ``with nål.running_stitch(30)`` og ``with nål.jump_stitch()`` konteksthåndterere som bestemmer hvilken søm skilpadde skal sy med mens den beveger seg.
Konteksthåndterere i Python brukes når vi har noe som består av en startinstruks og en sluttinstruks.
I vårt tilfelle er det å starte og avslutte en sømtype. Bak scenen blir

.. include-turtlethread:: stitch_types/10.py
    :linenos:
    :emphasize-lines: 4

Det samme som 

.. include-turtlethread:: stitch_types/11.py
    :linenos:
    :emphasize-lines: 4,6

Men det anbefales å bruke konteksthåndtereren i de aller fleste tilfeller fordi det er ryddigere og det garanterer at man alltid avslutter den sømmetypen man har startet på. 
