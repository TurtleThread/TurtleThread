.. _for_nb_NO:

For løkker
----------

Gjentakelser og repetisjon dukker ofte opp i både natur, kunst og arkitektur. Og det som er så praktisk er at datamaskinen er spesielt godt egnet til å repetere.
Den kan gjøre det samme tusenvis av ganger, ja hundretusenvis av ganger, uten å bli lei.

.. figure:: /figures/manual_examples/for/pexels-visually-us-2248572.jpg
    :figwidth: 32.5%

    Natur

    Nærbilde av en kaktus sine pigger (`bilde av Visually Us <https://www.pexels.com/photo/spikes-of-a-cactus-2248572/>`_).


.. figure:: /figures/manual_examples/for/pexels-magda-ehlers-4239915.jpg
    :figwidth: 32.5%

    Kunst

    Trykk på stoff (`bilde av Magda Ehlers <https://www.pexels.com/photo/white-pink-and-green-floral-textile-4239915/>`_).

.. figure:: /figures/manual_examples/for/pexels-david-underland-3432813.jpg
    :figwidth: 32.5%

    Arkitektur

    Svart-hvitt bilde av en bygning (`bilde av David Underland <https://www.pexels.com/photo/grayscale-photo-of-a-building-3432813//>`_).

Når vi programmerer, kan vi bruke løkker for å gjenta en bit kode mange ganger uten å skrive den samme koden flere ganger.
I Python finnes det to typer løkker: ``for``-løkker og ``while``-løkker.
I denne guiden skal vi se på ``for`` løkker. Først, la oss se på et eksempel:


.. include-turtlethread:: for/01.py
    :linenos:

.. image:: for/manual_code_output/01.svg
  :width: 100
  :alt: Resultat fra koden over. En "stjerne" bestående av seks streker som kommer ut fra samme punkt.
  :class: sphx-glr-script-out


Denne koden kan vi forenkle med en ``for``-løkke

.. include-turtlethread:: for/02.py
    :linenos:
    :emphasize-lines: 5-8 

.. image:: for/manual_code_output/02.svg
  :width: 100
  :alt: Resultat fra koden over. En "stjerne" bestående av seks streker som kommer ut fra samme punkt.
  :class: sphx-glr-script-out

Vi ser at den nye koden er mye kortere, og kanskje til og med litt enklere å forstå. Det viktige å forstå på er det som skjer på linje 5-9.

:Linje 5: Sier vi at vi skal repetere den etterfølgende *kodeblokka* 6 ganger, en gang for hver stråle.
:Linje 6-9: Disse linjene ligger ett innrykk inn sammenliknet med ``for``-løkka som startet på linje 5, og representerer derfor en kodeblokk. Disse tre linjene blir dermed repetert 6 ganger.


.. admonition:: Prøv selv:

    Modifiser koden over slik at du tegner en stjerne med åtte stråler istedenfor 6 (hint: Da må det være 45° mellom hver stråle).

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: for/03.py
            :linenos:
            :emphasize-lines: 5, 8
        
        
        .. image:: for/manual_code_output/03.svg
            :width: 90
            :alt: Resultat fra koden over. En "stjerne" bestående av åtte streker som kommer ut fra samme punkt.
            :class: sphx-glr-script-out

.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.



Mer om ``range``
~~~~~~~~~~~~~~~~

Foreløpig har vi hoppet litt over hva selve ``range``-funksjonen gjør.
Hvis vi leser koden over står det jo ``for stråle in range(8)``. Altså for hver stråle i ``range(8)``.
Å skrive ``range(8)`` blir litt som å be Python generere listen ``[0, 1, 2, 3, 4, 5, 6, 7]``.
Vi kan se dette i praksis ved å skrive ut variabelen ``stråle`` i terminalvinduet

.. include-turtlethread:: for/04.py
    :linenos:
    :emphasize-lines: 9

.. image:: for/manual_code_output/04.svg
  :width: 100
  :alt: Resultat fra koden over. En "stjerne" bestående av åtte streker som kommer ut fra samme punkt.
  :class: sphx-glr-script-out
 
Vi ser altså at ``range``-funksjonen skaper en rekke med heltall frem til, men ikke med, avslutningstallet, som i dette tilfellet var 6. Og at ``stråle`` blir en variabel som løkker seg igjennom rekka.

.. sidebar:: Sidespor: Hvorfor har linje 6-9 ekstra innrykk?

    Innrykk er det Python bruker for å gruppere kodelinjer sammen i *kodeblokker*. 
    Når vi starter en løkke med f.eks. ``for stråle in range(8)``, må vi også definere en *kodeblokk* rett under som inneholder de kodelinjene som skal kjøres for hver runde i løkka.
    Alt som skal gjentas i løkka må altså være på samme innrykknivå. 
    Under er to eksempler, et hvor skilpadden går frem og tilbake 8 ganger, men roterer bare en gang etter løkka 
    og et slik at skilpadden går frem 8 ganger, men går tilbake og roterer bare en gang etter løkka. 

    .. image:: for/manual_code_output/05.svg
        :width: 180
        :alt: Resultat fra koden under. En kort rett strek hvor "skilpadda" er i venstre kant av streken.

    .. collapse:: Kode:

        .. include-turtlethread:: for/05.py
            :linenos:
            :emphasize-lines: 8, 9

    .. image:: for/manual_code_output/06.svg
        :width: 180
        :alt: Resultat fra koden under. En lengre rett strek hvor "skilpadda" er nesten i høyre kant av streken.

    .. collapse:: Kode:
        
        .. include-turtlethread:: for/06.py
            :linenos:
            :emphasize-lines: 7, 8, 9

        
    .. attention:: 

       Legg merke til at alle linjene under ``with nål.running_stitch(25):`` også har ett innrykk inn. Dette definerer en kodeblokk av linjer som skal sys med rettsøm. 
       Dette kan du lese mer om `her <../auto_examples/gallery_introduksjon.html>`_.


Siden stråle blir en variabel, kan vi bruke den i tegningen vår. Hvis vi for eksempel ønsker at strålene våre skal ha ulik lengde, kan vi bruke ``stråle``-variabelen til å sette lengden.

.. include-turtlethread:: for/07.py
    :linenos:

.. image:: for/manual_code_output/07.svg
    :width: 10
    :alt: Resultat fra koden over. Syv veldig små streker med ulik størrelse som danner en "ministjerne". Det er nesten umulig å se detaljer siden strekene er så korte.
    :class: sphx-glr-script-out

Men dette var jo ikke det vi ønsket! Her fikk vi jo en bitteliten figur hvor alle stingene ble satt i samme sted. 
Dette skjedde siden ``stråle``-variabelen tross alt kun har verdier mellom 0 og 5. 
Vi vil jo ha lengre stråler enn som så. 
Og for å få til det må vi bruke en annen funksjonalitet til ``range``-funksjonen. 
range kan nemlig også bestemme hvor tallrekka starter, og hvor stor avstand det skal være mellom hver stråle. 
Så hvis vi ønsker at den minste strålen skal ha lengde 50, den største strålen skal ha lengde 225 og at det skal være 25 "steg" mellom hvert strålenummer kan vi skrive

.. include-turtlethread:: for/08.py
    :linenos:
    :emphasize-lines: 5

.. image:: for/manual_code_output/08.svg
    :width: 150
    :alt: Resultat fra koden over. En stjerne bestående av åtte streker med økende størrelse. Den korteste streken peker til høyre, så øker de i lengde jo lengre man beveger seg med klokka.
    :class: sphx-glr-script-out


Det interessante her er på linje 5 igjen. Vi ser at det nå står ``range(50, 250, 25)``. Dette betyr altså at vi starter tallrekka på 50, den slutter før 250 og det er 25 steg mellom hvert tall. 

.. admonition:: Prøv selv:

    Modifiser koden over slik at den minste strålen har lengde 100, den lengste har lengde 400 og det er 50 steg mellom hvert strålenummer.

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: for/09.py
            :linenos:
            :emphasize-lines: 5, 8
        
        
        .. image:: for/manual_code_output/09.svg
            :width: 90
            :alt: Resultat fra koden over. En stjerne bestående av åtte streker med økende størrelse. Den korteste streken peker til høyre, så øker de i lengde jo lengre man beveger seg med klokka.


Vi kan bruke denne teknikken for å tegne enda litt kulere stjerner. For eksempel, hvis antall grader vi roterer nåla er 150 vil vi få denne figuren:

.. include-turtlethread:: for/10.py
    :linenos:
    :emphasize-lines: 8

.. image:: for/manual_code_output/10.svg
    :width: 150
    :alt: Resultat fra koden over. En stjerne bestående av åtte streker med ulik størrelse, tilsynelatende uten mønster om hvilke streker som er korte og lange.
    :class: sphx-glr-script-out

.. attention:: 

    Hvis du lager mange stråler så kan stingene i sentrum bli for tette til at broderimaskinen klarer å sy.

TODO: lenke til flere eksempler:
•	Firkantblomst
•	Snøfnugg
•	Fibonacci
•	Evt Solsikkefrø
•	Evt andre
