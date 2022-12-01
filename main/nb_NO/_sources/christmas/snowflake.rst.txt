.. _christmas-rotation-symmetry:

Julekuler, snøflak og rotasjonssymmetri
---------------------------------------

I denne guiden skal vi lære hvordan dekorere julepynt med snøfnuggbroderi i Python. Bildet under viser et eksempel på julepynten vi skal lage med programmering.

.. image:: /../../_static/figures/manual_examples/snowflake/embroidered_rotational_snowflake.jpg
    :width: 400
    :alt: Et brodert snøfnugg


.. admonition:: Notis
    
    Denne guiden antar at du har turtlethread installert fra før. Hvis du ikke har det, :ref:`kan du trykke her for instrukser<installasjon>`. 


Et klassisk og vakkert motiv for julepynt er et snøfnugg. Hva er det som gjør snøfnugg så dekorative? 

.. figure:: /../../_static/figures/manual_examples/snowflake/SIA-SIA2013-09130.jpg
    :figwidth: 50%

    Snøfnugg (`Bilde av Wilson Alwyn Bentley (1865-1931) <https://www.si.edu/object/wilson-bentley-photomicrograph-stellar-snowflake-no-990:siris_arc_308076>`_).

Ser vi nærmere på snøfnugget over ser vi at et av kjennetegnene er at det er symmetrisk. Det har for eksempel *rotasjonssymmetri* som vil si at det ser likt ut
(med unntak av små "skader") når vi roterer rundt sentrum. Rotasjonssymmetri er både dekorativt og resurssparende og er mye brukt i både natur, matematikk, design og kunst. 

.. figure:: /../../_static/figures/manual_examples/snowflake/pexels-julia-volk-7293094.jpg
    :figwidth: 24%

    Natur

    Sjøstjerne (`bilde av Julia Volk <https://www.pexels.com/photo/red-starfish-on-sandy-bottom-of-clear-sea-7293094/>`_).

.. figure:: /../../_static/figures/manual_examples/snowflake/3-7_kisrhombille.svg
    :figwidth: 24%

    Matematikk

    Illustrasjon av et matematisk konsept (`illustrasjon av Parcly Taxel <https://commons.wikimedia.org/wiki/File:3-7_kisrhombille.svg>`_)

.. figure:: /../../_static/figures/manual_examples/snowflake/pexels-andreea-ch-1040895.jpg
    :figwidth: 24%

    Kunst

    Rom med fargerike fliser (`bilde av Andreea Ch <https://www.pexels.com/photo/room-with-multicolored-wall-tiles-1040895/>`_)

.. figure:: /../../_static/figures/manual_examples/snowflake/pexels-humphrey-muleba-2271568.jpg
    :figwidth: 24%

    Teknologi

    Drone (`bilde av Humphrey Muleba <https://www.pexels.com/photo/person-holding-gray-and-black-quadcopter-drone-2271568/>`_)

Pynt til jul med snøkrystallbroderi i Python!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Brodere en strek
~~~~~~~~~~~~~~~~

Begynn med å kopiere koden under inn i kodeeditoren din og kjør den. Hva blir tegnet opp på skjermen?


.. include-turtlethread:: snowflake/01.py
    :linenos:

.. image:: snowflake/manual_code_output/01.svg
    :width: 100
    :alt: Resultat fra koden over. En horisontal blå strek med tre korte vertikale streker, en i hver ende og en på midten.
    :class: sphx-glr-script-out

La oss gå igjennom koden linje for linje: 


:Linje 1: Importerer Turtle kommandoen fra turtlethread biblioteket. Dette er litt som å be Python om å gå inn i verktøyboden og hente frem det verktøyet (``Turtle``) vi trenger og legge det frem på arbeidsbenken. 
:Linje 3: Bruker Turtle kommandoen til å lage et Turtle objekt og lagre det i en variabel ved navn ‘nål’. Dette er det vi skal bruke for å brodere. 
:Linje 4: Forteller hva slags søm vi skal bruke. For mer om søm i turtlethread kan du klikke her, men alt du trenger å vite for nå er at vi i denne linjen ber om en *rettsøm* (``running_stitch``) med *5 mm* (50 steg) mellom hvert sting.
:Linje 5: Ber nåla om å bevege seg fremover 100 steg. Legg merke til at denne koden ligger inne i et *innrykk* etter ``with nål.running_stitch(50):`` linja, som betyr at nåla skal brodere mens den beveger seg.
:Linje 7: Kaller på nåla sin ``visualise`` funksjon. Denne funksjonen ber Python tegne hvordan broderiet kommer til å se ut og er en fin måte å sjekke om mønsteret blir riktig før du prøver å brodere på stoff. 
:Linje 2 og 6: Er tomme. Tomme linjer brukes til å gjøre koden ryddigere og enklere å lese, men har ikke noe å si for programmet. Du kan fjerne dem uten at det har noen effekt. 

.. admonition:: Prøv selv:

    * Endre programmet slik at det har en søm med 30 steg mellom hvert sting. Kjør programmet, ser du forskjellen?
    * Endre programmet slik at nåla beveger seg 90 steg fremover istedenfor 100 steg fremover.

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: snowflake/02.py
            :linenos:
        
        
        .. image:: snowflake/manual_code_output/02.svg
            :width: 90
            :alt: Resultat fra koden over. En horisontal blå strek med fire korte vertikale streker med lik avstand mellom hver strek.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.


Snu til høyre
~~~~~~~~~~~~~

Vi vil at "armene" til snøkrystallen skal ha "grener". For å få til det må vi rotere skilpadden, det kan vi gjøre med right kommandoen. Programmet under tegner en gren med 45° rotasjon og steglengde 90:

.. include-turtlethread:: snowflake/03.py
    :linenos:

.. image:: snowflake/manual_code_output/03.svg
    :width: 154
    :alt: Resultat fra koden over. En horisontal blå strek og en diagonal strek som starter i høyre ende av den horisontale streken. Strekene har små streker på tvers med lik avstand mellom hver tverrstrek.
    :class: sphx-glr-script-out

    
:Linje 5 og 8: Starter med et ``#`` symbol som betyr at her kommer en kommentar som Python skal ignorere. Slike kommentarer bruker vi for å holde programmet ryddig med små forklaringer. 
:Linje 9: Roterer skilpadden 45 grader mot høyre.

.. admonition:: Prøv selv:

    * Kjør programmet og se hva du får ut 
    * Endre programmet slik at grenen er rotert 30 grader istedenfor 45
    * Endre programmet slik at grenen har lengde 60 istedenfor 90

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: snowflake/04.py
            :linenos:

        .. image:: snowflake/manual_code_output/04.svg
            :width: 168
            :alt: Resultat fra koden over. En horisontal blå strek og en diagonal strek som starter i høyre ende av den horisontale streken.
                Strekene har små streker på tvers med lik avstand mellom hver tverrstrek.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.

Fullføre armen på snøfnugget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Etter å ha tegnet "grenen" må vi rygge bakover og rotere tilbake for å fortsette på armen. Dette kan vi gjøre med ``backward`` og ``left`` slik:


.. include-turtlethread:: snowflake/05.py
    :linenos:

.. image:: snowflake/manual_code_output/05.svg
    :width: 180
    :alt: Resultat fra koden over. En lang horisontal blå strek og en diagonal strek som starter i midten av den lange streken og går litt nedover.
        Strekene har små streker på tvers med lik avstand mellom hver tverrstrek.
    :class: sphx-glr-script-out


.. admonition:: Prøv selv:

    * Kjør programmet og se hva du får ut.
    * Hvorfor er tallet i linje 10 og 11 likt. Er dette viktig? Hvorfor/Hvorfor ikke?


Nå fullfører vi armen ved å gå bakover og tegne en gren på andre siden også. Det er viktig at vi slutter med nåla i samme posisjon og pekende i samme retning som når vi startet:

.. include-turtlethread:: snowflake/06.py
    :linenos:

.. image:: snowflake/manual_code_output/06.svg
    :width: 180
    :alt: Resultat fra koden over. En lang horisontal blå strek og to diagonale streker som starter i midten av den lange streken og går litt nedover og oppover.
        Strekene har små streker på tvers med lik avstand mellom hver tverrstrek.
    :class: sphx-glr-script-out


.. admonition:: Prøv selv:
    
    * Kjør programmet og se hva du får ut.
    * Hva gjør linje 19 til 22?

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.

Bruke løkker til å tegne snøflak
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nå har vi et program som instruerer skilpadden vår til å brodere en snøkrystallarm.
Men snøkrystaller har gjerne flere armer, så får å tegne hele krystallen må vi gjenta disse kommandoene flere ganger.
For det kan vi bruke en løkke.
En mer detaljert forklaring på løkker i Python finner du :ref:`her <for>`, men for nå er alt du trenger å vite at vi kan bruke en forløkke for å tegne fire armer slik:

.. include-turtlethread:: snowflake/07.py
    :linenos:
    :emphasize-lines: 6, 30

.. image:: snowflake/manual_code_output/07.svg
    :width: 360
    :alt: Resultat fra koden over. Et snøfnugg med fire "armer". Hver arm er lik bildet fra forrige kodebit.
    :class: sphx-glr-script-out

De eneste nye linjene i dette programemt er linje 6 og 30. 

.. sidebar:: Side-track: Why did the turtle need to return to the starting point?
    
        If the turtle didn't end with the same position and rotation after drawing the arm, we would not be able to use a for loop to draw the snowflake.
        Below are two examples: one where the turtle ends up at the wrong position and one where it ends up with the wrong rotation. 

        .. image:: snowflake/manual_code_output/09.svg
            :width: 180
            :alt: Resultat fra koden over. Forsøk på å tegne snøfnugg hvor vi ikke drar tilbake til start for hver arm.

        .. collapse:: Kode:

            .. include-turtlethread:: snowflake/09.py
                :linenos:

        .. image:: snowflake/manual_code_output/10.svg
            :width: 180
            :alt: Resultat fra koden over. Forsøk på å tegne snøfnugg hvor vi ikke roterer mellom hver arm, da blir alle armene tegnet oppå hverandre slik at det ser ut som om det kun er en arm.

        .. collapse:: Kode:
            
            .. include-turtlethread:: snowflake/10.py
                :linenos:

:Linje 6: Definerer en ``for`` løkke og forteller python at alt som skjer inne i løkka skal gjentas 4 ganger.
    Legg merke til at linjene 7-30 har blitt flyttet ett innrykk inn.
    Det forteller python at disse linjene er inne i løkka og skal gjentas for hver runde i løkka
:Linje 30: Ber skilpadden om å rotere 90 grader for hver runde i løkka. Denne linja trenger vi for at snøkrystallarmene ikke skal tegnes oppå hverandre. 

.. admonition:: Prøv selv:
    
    * Kjør programmet og se hva du får ut
    * Hvorfor roterer det 90 grader i linje 30? Hva skjer om du endrer til 60?
    * Endre programemt slik at det tegner en snøkrystall med 6 armer istedenfor 4

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: snowflake/08.py
            :linenos:

        .. image:: snowflake/manual_code_output/08.svg
            :width: 360
            :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.

Nå har vi kode for å tegne et helt snøfnugg! 

.. admonition:: Prøv selv:
    
    Bruk kode til å tegne dit eget snøfnugg med rotasjonssymmetri. Under er et galleri med noen eksempler til inspirasjon:

Lage en julekule med snøflakmønster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /../../_static/figures/manual_examples/snowflake/actionshot.jpg
    :width: 400
    :alt: Et bilde av broderimaskinen mens den lager et snøfnugg.

For å lage juletrepynt med snøflakbroderiet må du først lagre mønsteret som en broderifil.
Dette kan du gjøre ved å legge til

.. code:: python
    
    nål.save("snøflak.jef")

på slutten av scriptet ditt.
Merk at vi her bruker ``.jef``-filtypen, som vi har funnet ut at virker bra med Bernina 500 broderimaskinen vi har brukt, men du vil kanskje bruke en annen filtype for din maskin (f.eks. ``snøflak.pes``).
Når du har lagd broderifilen kan du følge disse instruksene for å lage en julekule:

1. Broder ett eller to snøfnugg, avhengig av om du vil ha snøfnugg på begge sidene av julekulen,
2. legg de to stoffbitene oppå hverandre slik at broderiene er rett over hverandre og peker utover,
3. og sy sammen stoffbitene (enten for hånd eller ved å tegne en sirkel med turtlethread).


Eksempelsnøflak
^^^^^^^^^^^^^^^

**Snøflak 1**

.. image:: snowflake/manual_code_output/gallery01.svg
    :width: 180
    :alt: To armer av ulike snøflak oppå hverandre (med 30 graders rotasjon mellom de to armene).
        Den en arm-typen består av en lang linje med tre sirkler av ulik størrelse på enden.
        Den andre arm-typen består av en liten strek med en liten sirkel på enden.
    :class: snowflake-gallery-arm

.. collapse:: Snøflak
    :class: snowflake-gallery-snowflake

    .. image:: snowflake/manual_code_output/gallery01_full.svg
        :width: 360 
        :alt: To snøflak oppå hverandre som danner et snøflak med tolv armer av alternerende utseende.
            Den en arm-typen består av en lang linje med tre sirkler av ulik størrelse på enden.
            Den andre arm-typen består av en liten strek med en liten sirkel på enden.


.. collapse:: Kode for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery01.py
        :linenos:

.. collapse:: Kode for snøflak
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery01_full.py
        :linenos:


**Snøflak 2**

.. image:: snowflake/manual_code_output/gallery02.svg
    :width: 180
    :alt: En rettvinklet trekant hvor hypotenusen er horisontal.
        Katetenes forhold til hypotenusen er 3/5 og 4/5.
    :class: snowflake-gallery-arm

.. collapse:: Snøflak
    :class: snowflake-gallery-snowflake

    .. image:: snowflake/manual_code_output/gallery02_full.svg
        :width: 360
        :alt: Et snøflak med armer som er rettvinklede trekanter.
            Det ser ut som en papir-vindmølle.


.. collapse:: Kode for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery02.py
        :linenos:

.. collapse:: Kode for snøflak
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery02_full.py
        :linenos:


**Snøflak 3**

.. image:: snowflake/manual_code_output/gallery03.svg
    :width: 180
    :alt: To armer av ulike snøflak oppå hverandre (med 30 graders rotasjon mellom).
        Begge armene likner på de i guiden, men har ulik størrelse.
    :class: snowflake-gallery-arm

.. collapse:: Snøflak
    :class: snowflake-gallery-snowflake

    .. image:: snowflake/manual_code_output/gallery03_full.svg
        :width: 360
        :alt: To snøflak oppå hverandre som danner et snøflak med tolv armer av alternerende utseende.
            Begge snøflakene har armer som likner på de i guiden, men med ulik størrelse.


.. collapse:: Kode for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery03.py
        :linenos:

.. collapse:: Kode for snøflak
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery03_full.py
        :linenos: