Julekuler, stjernehimler og tilfeldighet
----------------------------------------

**TODO: Tegn stjernehimmel**

Hvilken av de to stjernehimlene over ser mest "naturlig" ut? Når vi lager kunst med programmering, blir tegningene våre fort veldig ryddige og perfekte.
Dette kan føre til veldig vakre mønstere, men naturen er ikke helt perfekt, så det kan også se litt "kunstig" ut.
Et triks for å få litt av naturens "ikke-perfekthet" inn in kodekunsten vår er å bruke tilfeldighet.
Å legge på litt tilfeldighet er en teknikk som er hyppig brukt i bildekunst, spilldesign, animasjon og musikk

.. figure:: /../../_static/figures/manual_examples/randomness/10print.svg
    :figwidth: 24%

    Bildekunst

    Generativ kunst, variant 10print.

.. figure:: /../../_static/figures/manual_examples/randomness/600px-Tiling_procedural_textures.jpg
    :figwidth: 24%

    Prosedurale teksturer for dataspill

    Illustrasjon av proseduralt genererte teksturer (`illustrasjon av Drummyfish <https://en.wikipedia.org/wiki/File:Tiling_procedural_textures.jpg>`_)


.. figure:: /../../_static/figures/manual_examples/randomness/Terragen.jpg
    :figwidth: 24%

    Proseduralt landskap

    Proseduralt generert landskapsbilde (`illustrasjon av Levyznin <https://en.wikipedia.org/wiki/File:Terragen.jpg>`_)


.. figure:: /../../_static/figures/manual_examples/randomness/5612345200_a45d40bccb_c.jpg
    :figwidth: 24%

    Musikk

    Bilde av en modulær sythesizer. Slike kan ofte spille av lydsekvenser i en tilfeldig rekkefølge (`Bilde av Muff på Flickr (CC-BY 2.0) <https://www.flickr.com/photos/61547250@N02/5612345200>`_)

Det første vi kan starte med er å se hvordan vi kan lage tilfeldige tall i Python. Nedenfor er en kodesnutt som printer ut et tilfeldig tall.

.. include-turtlethread:: tilfeldighet/01.py
    :linenos:
    :emphasize-lines: 1,3

:Linje 1: Importerer ``random``-biblioteket som vi kan bruke for å trekke tilfeldige tall.
:Linje 3: Bruker ``random.randint``-funksjonen til å trekke et tilfeldig tall fra og med ``1`` til og med ``6`` og lagrer dette tilfeldige tallet i ``tilfeldig_tall``-variabelen. 

.. admonition:: Prøv selv:

    * Kjør koden mange ganger. Får du forskjellig hver gang?
    * Endre så det istedenfor gir et tall mellom 50 og 100
    * Kjør koden mange ganger igjen, får du andre tall ut nå?

Dette kan vi bruke for å gjøre broderiene våre mer spennende.
Her er kode for å generere en enkel stjerne

.. include-turtlethread:: tilfeldighet/02.py
    :linenos:

.. image:: tilfeldighet/manual_code_output/02.svg
    :width: 180
    :alt: En enkel stjerne med seks stråler.
    :class: sphx-glr-script-out

For å gjøre den mer naturlig og interessant kan vi legge på litt tilfeldighet på lengden til strålene:

.. include-turtlethread:: tilfeldighet/03.py
    :linenos:
    :emphasize-lines: 7
    
.. image:: tilfeldighet/manual_code_output/03.svg
    :width: 180
    :alt: En enkel stjerne med seks stråler som hver har litt ulik lengde.
    :class: sphx-glr-script-out

:Linje 7: Trekker et tilfeldig tall mellom 80 og 120 og lagrer det i ``strålelengde`` variabelen.

Her ser vi at stjernen ser litt mer tilfeldig ut og dermed også litt mer naturlig.

.. admonition:: Prøv selv:

    * Endre så stråle-lengden er mellom 25 og 125 istedenfor 80 og 120. Hvordan endrer dette uttrykket til stjernen?
    * Endre koden slik at antall stråler også er et tilfeldig tall. (**HINT:** Vinkelen mellom hver stråle må være ``360 / antall_stråler``)
    
    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: tilfeldighet/04.py
            :linenos:
            :emphasize-lines: 6-8
        
        .. image:: tilfeldighet/manual_code_output/04.svg
            :width: 180
            :alt: Resultat fra koden over. En stjerne med et tilfeldig antall stråler og tilfeldig lengde på hver stråle.
            :class: sphx-glr-script-out


.. attention:: 

    Pass på at koden stemmer med løsningsforslaget over før du går videre.

Nå har vi tegnet en tilfeldig stjerne, men vi kan ta det hele ett steg lengre ved å tegne flere tilfeldige stjerner plassert tilfeldig over en stjernehimmel.
Vi kan f.eks. bruke ``goto``-kommandoen og la nåla gå til en tilfeldig plass på stoffet for hver stjerne.
Koden nedenfor tegner en stjernehimmel med fire tilfeldige stjerner plassert tilfeldig ut over stjernehimmelen.

.. include-turtlethread:: tilfeldighet/05.py
    :linenos:
    :emphasize-lines: 6-10
    
.. image:: tilfeldighet/manual_code_output/05.svg
    :width: 360
    :alt: Resultat fra koden over.
        Et sett med fire stjerner, hver plassert tilfeldig på skjermen med et tilfeldig antall stråler og tilfeldig lengde.
        Det er en søm mellom hver stjerne
    :class: sphx-glr-script-out

:Linje 6: Definerer en antall_stjerner variabel som sier hvor mange stjerner vi ønsker å tegne
:Linje 7: Starter løkka vi bruker for å tegne flere stjerner
:Linje 8-9: Trekker tilfeldige koordinater mellom ``-250`` og ``250`` for hver av stjernene våre
:Linje 10: Beveger nåla til den tilfeldige posisjonen hver av stjernene skal ha

Her har vi en fin, tilfeldig stjernehimmel!
Men nå broderer vi også en linje mellom stjernene. 
Det kan gi en kul effekt som kanskje kan minne om stjernetegn, men hvis vi ikke ønsker å ha en slik linje kan vi bruke jump stitch til å la nåle hoppe uten å sy mellom hver stjerne. 


.. include-turtlethread:: tilfeldighet/06.py
    :linenos:
    :emphasize-lines: 6-7,10,13

    
.. image:: tilfeldighet/manual_code_output/06.svg
    :width: 360
    :alt: Resultat fra koden over.
        Et sett med fire stjerner, hver plassert tilfeldig på skjermen med et tilfeldig antall stråler og tilfeldig lengde.
        Nå er stjernene koblet sammen med en rød strek som symboliserer at nåla skal "hoppe over" denne biten. Det er også en rød sirkel i midten av hver stjerne, som symboliserer starten på en ny søm.
    :class: sphx-glr-script-out

:Linje 6-7: Løkka som itererer over stjernene er flyttet ut av kodeblokka hvor nåla har sømmeinstrukser.
    Vi flytta løkka siden vi ønsker å bruke forskjellige sømmeinstrukser når vi tegner stjernene og når vi flytter nåla mellom stjernene.
:Linje 10: Gir nåla instruks om å flytte seg uten å sy sting.
    Dersom broderimaskina støtter det vil den klippe tråden om den allerede har sydd noen sting.
:Linje 13: Her er kodeblokka hvor vi tegner hver enkelt stjerne.


.. admonition:: Prøv selv:
    
    Endre koden slik at du tegner et tilfeldig antall stjerner på stjernehimmelen
    
    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: tilfeldighet/07.py
            :linenos:
            :emphasize-lines: 6
            
        .. image:: tilfeldighet/manual_code_output/07.svg
            :width: 360
            :alt: Resultat fra koden over.
                Et sett med et tilfeldig antall stjerner, hver plassert tilfeldig på skjermen med et tilfeldig antall stråler og tilfeldig lengde.
                Nå er stjernene koblet sammen med en rød strek som symboliserer at nåla skal "hoppe over" denne biten. Det er også en rød sirkel i midten av hver stjerne, som symboliserer starten på en ny søm.
            :class: sphx-glr-script-out

.. attention:: 

    I dette eksempelet bruker vi ``randint``-funksjonen i ``random``-biblioteket, som trekker tall fra og med første argument, til og med andre argument.
    Hvis vi istedenfor hadde brukt ``randint``-funksjonen i ``numpy.random`` eller ``pylab``, så ville vi ikke kunne fått det andre argumentet.
    For eksempel vil ``random.randint(1, 6)`` gi oss et av tallene 1, 2, 3, 4, 5 eller 6, mens ``numpy.random.randint(1, 6)`` og ``pylab.randint(1, 6)`` vil bare gi oss et av tallene 1, 2, 3, 4 eller 5.

**TODO TEKST OM TILFELDIGHETSGALLERI**

Eksempelbroderi med tilfeldighet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Eksempel 1**

.. image:: tilfeldighet/manual_code_output/gallery01.svg
    :width: 180
    :alt: En spiral hvor hver linje har tilfeldig, men økende, lengde.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: tilfeldighet/gallery01.py
        :linenos:


**Eksempel 2**

.. image:: tilfeldighet/manual_code_output/gallery02.svg
    :width: 180
    :alt: Tilfeldig plasserte sirkler med en strek mellom hver sirkel.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: tilfeldighet/gallery02.py
        :linenos:



**Eksempel 3**

.. image:: tilfeldighet/manual_code_output/gallery03.svg
    :width: 180
    :alt: Et snøflak med armer som har tilfeldig lengde og et tilfeldig antall grener på hver arm.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: tilfeldighet/gallery03.py
        :linenos:
        

**Eksempel 4**

.. image:: tilfeldighet/manual_code_output/gallery04.svg
    :width: 180
    :alt: Et juletre hvor lengden og vinkelen til hver gren er litt tilfeldig.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: tilfeldighet/gallery04.py
        :linenos:

**TODO: Alt text**