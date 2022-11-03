.. _sneflak:

Julekuler, snøflak og rotasjonssymmetri
---------------------------------------

I denne guiden skal vi lære hvordan dekorere julepynt med snøfnuggbroderi i Python. Bildet under viser et eksempel på julepynten vi skal lage med programmering.

[TODO: legg inn bilde]

.. admonition:: Notis
    
    Denne guiden antar at du har turtlethread installert fra før. Hvis du ikke har det, :ref:`kan du trykke her for instrukser<installasjon>`. 


Et klassisk og vakkert motiv for julepynt er et snøfnugg. Hva er det som gjør snøfnugg så dekorative? 

.. figure:: /figures/manual_examples/snowflake/SIA-SIA2013-09130.jpg
    :figwidth: 50%

    Snøfnugg (`Bilde av Wilson Alwyn Bentley (1865-1931) <https://www.si.edu/object/wilson-bentley-photomicrograph-stellar-snowflake-no-990:siris_arc_308076>`_).

Ser vi nærmere på snøfnugget over ser vi at et av kjennetegnene er at det er symmetrisk. Det har for eksempel *rotasjonssymmetri* som vil si at det ser likt ut
(med unntak av små "skader") når vi roterer rundt sentrum. Rotasjonssymmetri er både dekorativt og resurssparende og er mye brukt i både natur, matematikk, design og kunst. 

.. figure:: /figures/manual_examples/snowflake/pexels-julia-volk-7293094.jpg
    :figwidth: 24%

    Natur

    Sjøstjerne (`bilde av Julia Volk <https://www.pexels.com/photo/red-starfish-on-sandy-bottom-of-clear-sea-7293094/>`_).

.. figure:: /figures/manual_examples/snowflake/3-7_kisrhombille.svg
    :figwidth: 24%

    Matematikk

    Illustrasjon av et matematisk konsept (`illustrasjon av Parcly Taxel <https://commons.wikimedia.org/wiki/File:3-7_kisrhombille.svg>`_)

.. figure:: /figures/manual_examples/snowflake/pexels-andreea-ch-1040895.jpg
    :figwidth: 24%

    Kunst

    Rom med fargerike fliser (`bilde av Andreea Ch <https://www.pexels.com/photo/room-with-multicolored-wall-tiles-1040895/>`_)

.. figure:: /figures/manual_examples/snowflake/pexels-humphrey-muleba-2271568.jpg
    :figwidth: 24%

    Teknologi

    Drone (`bilde av Humphrey Muleba <https://www.pexels.com/photo/person-holding-gray-and-black-quadcopter-drone-2271568/>`_)

Pynt til jul med snøkrystallbroderi i Python!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Brodere en strek
~~~~~~~~~~~~~~~~

Begynn med å kopiere koden under inn i kodeeditoren din og kjør den. Hva blir tegnet opp på skjermen?


.. include-turtlethread:: sneflak/01.py
    :linenos:

.. image:: sneflak/manual_code_output/01.svg
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

        .. include-turtlethread:: sneflak/02.py
            :linenos:
        
        
        .. image:: sneflak/manual_code_output/02.svg
            :width: 90
            :alt: Resultat fra koden over. En horisontal blå strek med fire korte vertikale streker med lik avstand mellom hver strek.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.


Snu til høyre
~~~~~~~~~~~~~

Vi vil at "armene" til snøkrystallen skal ha "grener". For å få til det må vi rotere skilpadden, det kan vi gjøre med right kommandoen. Programmet under tegner en gren med 45° rotasjon og steglengde 90:

.. include-turtlethread:: sneflak/03.py
    :linenos:

.. image:: sneflak/manual_code_output/03.svg
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

        .. include-turtlethread:: sneflak/04.py
            :linenos:

        .. image:: sneflak/manual_code_output/04.svg
            :width: 168
            :alt: Resultat fra koden over. En horisontal blå strek og en diagonal strek som starter i høyre ende av den horisontale streken.
                Strekene har små streker på tvers med lik avstand mellom hver tverrstrek.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.

Fullføre armen på snøfnugget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Etter å ha tegnet "grenen" må vi rygge bakover og rotere tilbake for å fortsette på armen. Dette kan vi gjøre med ``backward`` og ``left`` slik:


.. include-turtlethread:: sneflak/05.py
    :linenos:

.. image:: sneflak/manual_code_output/05.svg
    :width: 180
    :alt: Resultat fra koden over. En lang horisontal blå strek og en diagonal strek som starter i midten av den lange streken og går litt nedover.
        Strekene har små streker på tvers med lik avstand mellom hver tverrstrek.
    :class: sphx-glr-script-out


.. admonition:: Prøv selv:

    * Kjør programmet og se hva du får ut.
    * Hvorfor er tallet i linje 10 og 11 likt. Er dette viktig? Hvorfor/Hvorfor ikke?


Nå fullfører vi armen ved å gå bakover og tegne en gren på andre siden også. Det er viktig at vi slutter med nåla i samme posisjon og pekende i samme retning som når vi startet:

.. include-turtlethread:: sneflak/06.py
    :linenos:

.. image:: sneflak/manual_code_output/06.svg
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
En mer detaljert forklaring på løkker i Python finner du :ref:`her <for_nb_NO>`, men for nå er alt du trenger å vite at vi kan bruke en forløkke for å tegne fire armer slik:

.. include-turtlethread:: sneflak/07.py
    :linenos:
    :emphasize-lines: 6, 30

.. image:: sneflak/manual_code_output/07.svg
    :width: 360
    :alt: Resultat fra koden over. Et snøfnugg med fire "armer". Hver arm er lik bildet fra forrige kodebit.
    :class: sphx-glr-script-out

De eneste nye linjene i dette programemt er linje 6 og 30. 

.. sidebar:: Side-track: Why did the turtle need to return to the starting point?
    
        If the turtle didn't end with the same position and rotation after drawing the arm, we would not be able to use a for loop to draw the snowflake.
        Below are two examples: one where the turtle ends up at the wrong position and one where it ends up with the wrong rotation. 

        .. image:: sneflak/manual_code_output/09.svg
            :width: 180
            :alt: Resultat fra koden over. Forsøk på å tegne snøfnugg hvor vi ikke drar tilbake til start for hver arm.

        .. collapse:: Kode:

            .. include-turtlethread:: sneflak/09.py
                :linenos:

        .. image:: sneflak/manual_code_output/10.svg
            :width: 180
            :alt: Resultat fra koden over. Forsøk på å tegne snøfnugg hvor vi ikke roterer mellom hver arm, da blir alle armene tegnet oppå hverandre slik at det ser ut som om det kun er en arm.

        .. collapse:: Kode:
            
            .. include-turtlethread:: sneflak/10.py
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

        .. include-turtlethread:: sneflak/08.py
            :linenos:

        .. image:: sneflak/manual_code_output/08.svg
            :width: 360
            :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.

Nå har vi kode for å tegne et helt snøfnugg! 

.. admonition:: Prøv selv:
    
    Bruk kode til å tegne dit eget snøfnugg med rotasjonssymmetri. Under er et galleri med noen eksempler til inspirasjon:

    TODO: galleri

Lage en julekule med snøflakmønster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For å lage en julekule med snøflakmønster gjør du følgende:

1. Brodere to snøfnugg (enten på samme stoff eller to forskjellige hvis du vil ha ulike sider),
2. legg de to stoffbitene oppå hverandre slik at broderiene er rett over hverandre og peker utover,
3. og sy sammen stoffbitene (enten for hånd eller ved å tegne en sirkel med turtlethread). Her er en guide til sying og sammensetning *TODO*.


Eksempelsnøflak
~~~~~~~~~~~~~~~

**TODO: Eksempelgalleri**