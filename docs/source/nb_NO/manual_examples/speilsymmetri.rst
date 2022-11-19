Julekuler, snøflak og speilsymmetri
-----------------------------------

Den observante leser av :ref:`sneflak` (som vi anbefaler at du leser først) har kanskje oppdaget at snøflak ofte har flere typer symmetri enn bare rotasjonssymmetri.
Snøflak har nemlig det som heter for speilsymmetri: Hvis vi speiler snøfnugget langs en "gren" vil det ikke endres. 

.. figure:: /../../_static/figures/manual_examples/reflection_symmetry/pexels-eberhard-grossgasteiger-12366087.jpg
    :figwidth: 99%

    Speilsymmetry

    Naturlandskap reflektert i vann (`bilde av Eberhard Grossgasteiger <https://www.pexels.com/photo/symmetrical-view-of-rocky-landscape-reflecting-in-a-pond-12366087/>`_).

Når vi tenger figurer med speilsymmetri kan vi bruke en løkke til å kutte ned antall linjer kode (sånn som vi allerede har gjort for rotasjonssymmetri).
Under er koden vi lagde for å tegne et snøfnugg i :ref:`sneflak`. Ser vi nøye etter så kan vi se at linje 11-14 og 21-24 er veldig like, men vinklene peker i motsatt retning


.. include-turtlethread:: speilsymmetri/01.py
    :linenos:
    :emphasize-lines: 11-14,21-24

.. image:: speilsymmetri/manual_code_output/01.svg
    :width: 360
    :alt: Resultat fra koden over. Et snøfnugg med seks "armer".
    :class: sphx-glr-script-out

For å utnytte speilsymmetrien i koden må vi først legge merke til at det å rotere 30 grader til venstre er det samme som å rotere -30 grader til høyre. 
Vi kan altså bytte ut ``left`` med ``right`` hvis vi gir negativt fortegn til vinkelen. 

.. include-turtlethread:: speilsymmetri/02.py
    :linenos:
    :emphasize-lines: 14, 21

.. image:: speilsymmetri/manual_code_output/02.svg
    :width: 360
    :alt: Resultat fra koden over. Et snøfnugg med seks "armer".
    :class: sphx-glr-script-out

Siden vi kan styre retning ved hjelp av fortegn kan vi også endre retning i en løkke ved å bruke en ``for`` løkke som setter en ``retning``-variabel til ``1`` og så ``-1``:

.. include-turtlethread:: speilsymmetri/03.py
    :linenos:
    :emphasize-lines: 7, 12, 15

.. image:: speilsymmetri/manual_code_output/03.svg
    :width: 360
    :alt: Resultat fra koden over. Det er likt bildet som ble generert av forrige kodesnutt.
    :class: sphx-glr-script-out

Her ser vi at koden ble mye kortere!


.. admonition:: Prøv selv:
    
    Bruk kode til å tegne dit eget snøfnugg med både rotasjonssymmetri og speilsymmetri. Under er et galleri med noen eksempler til inspirasjon:


Eksempelsnøflak
~~~~~~~~~~~~~~~

**Snøflak 1**

.. image:: speilsymmetri/manual_code_output/gallery01.svg
    :width: 180
    :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.
    :class: snowflake-gallery-arm

.. collapse:: Snøflak
    :class: snowflake-gallery-snowflake

    .. image:: speilsymmetri/manual_code_output/gallery01_full.svg
        :width: 360
        :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.


.. collapse:: Kode for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: speilsymmetri/gallery01.py
        :linenos:

.. collapse:: Kode for snøflak
    :class: snowflake-gallery-code

    .. include-turtlethread:: speilsymmetri/gallery01_full.py
        :linenos:


**Snøflak 2**

.. image:: speilsymmetri/manual_code_output/gallery02.svg
    :width: 180
    :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.
    :class: snowflake-gallery-arm

.. collapse:: Snøflak
    :class: snowflake-gallery-snowflake

    .. image:: speilsymmetri/manual_code_output/gallery02_full.svg
        :width: 360
        :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.


.. collapse:: Kode for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: speilsymmetri/gallery02.py
        :linenos:

.. collapse:: Kode for snøflak
    :class: snowflake-gallery-code

    .. include-turtlethread:: speilsymmetri/gallery02_full.py
        :linenos:


**Snøflak 3**

.. image:: speilsymmetri/manual_code_output/gallery03.svg
    :width: 180
    :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.
    :class: snowflake-gallery-arm

.. collapse:: Snøflak
    :class: snowflake-gallery-snowflake

    .. image:: speilsymmetri/manual_code_output/gallery03_full.svg
        :width: 360
        :alt: Resultat fra koden over. Et snøfnugg med seks "armer". Ellers er det likt bildet over.


.. collapse:: Kode for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: speilsymmetri/gallery03.py
        :linenos:

.. collapse:: Kode for snøflak
    :class: snowflake-gallery-code

    .. include-turtlethread:: speilsymmetri/gallery03_full.py
        :linenos:

        
# TODO: Alt text