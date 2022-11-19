.. _for_en:

For loops
---------

Repetition is often seen in both nature, art and architecture.
And the computer is particularly suited for repetitive tasks.
The computer can repeat the same actions over and over for thousands or even hundreds of thousands of times without getting tired. 


.. figure:: /figures/manual_examples/for/pexels-visually-us-2248572.jpg
    :figwidth: 32.5%

    Nature

    Close-up of the needles on a cactus (`photo by Visually Us <https://www.pexels.com/photo/spikes-of-a-cactus-2248572/>`_).


.. figure:: /figures/manual_examples/for/pexels-magda-ehlers-4239915.jpg
    :figwidth: 32.5%

    Art

    Art print on fabric (`photo by Magda Ehlers <https://www.pexels.com/photo/white-pink-and-green-floral-textile-4239915/>`_).

.. figure:: /figures/manual_examples/for/pexels-david-underland-3432813.jpg
    :figwidth: 32.5%

    Architecture 

    Black and white photo of a building (`photo by David Underland <https://www.pexels.com/photo/grayscale-photo-of-a-building-3432813//>`_).

When we program, we can use loops to repeat a piece of code several times without writing the same code multiple times.
Python supports two types of loops, for loops and while loops.
In this tutorial, we will use for loop. Let's start with an example:

.. include-turtlethread:: for/01.py
    :linenos:

.. image:: for/auto_figures/01.svg
  :width: 100
  :alt: TODO: ALT TEXT: Resultat fra koden over. En "stjerne" bestående av seks streker som kommer ut fra samme punkt.
  :class: sphx-glr-script-out

We can shorten this code with a ``for`` loop: 

.. include-turtlethread:: for/02.py
    :linenos:
    :emphasize-lines: 5-8 

.. image:: for/auto_figures/02.svg
  :width: 100
  :alt: TODO ALT TEXT: Resultat fra koden over. En "stjerne" bestående av seks streker som kommer ut fra samme punkt.
  :class: sphx-glr-script-out

We see that the modified code is much shorter and more readable. The most important lines to understand here are lines 5-9. 

:Line 5: Tells Python that the code block below should be repeated 6 times, one for each ray in the star. 
:Lines 6-9: These lines are indented one more level than the other lines and represent a code block. The code block is directly below the definition of the for loop. Therefore this code block belongs to the for loop, so these lines will be repeated for each loop iteration (6 times). 

.. admonition:: Try it yourself:

    Modify the code above so the star has eight rays instead of 6 (HINT: then there must be 45 degrees between each ray)

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: for/03.py
            :linenos:
            :emphasize-lines: 5, 8
        
        
        .. image:: for/auto_figures/03.svg
            :width: 90
            :alt: TODO ALT TEXT: Resultat fra koden over. En "stjerne" bestående av åtte streker som kommer ut fra samme punkt.
            :class: sphx-glr-script-out

.. attention:: 

    Make sure your code matches the finished code above before you proceed.

More on ``range``
^^^^^^^^^^^^^^^^^

So far, we haven't explained much about the ``range`` function.
If we read the code above, we see the line ``for ray in range(8)``, which means for each ray in "``range(8)``".
Typing ``range(8)`` is almost like asking Python to generate a list of numbers ``[0, 1, 2, 3, 4, 5, 6, 7]``.
We can see this in practice by printing the ``ray`` variable to the terminal for each loop iteration. 

.. include-turtlethread:: for/04.py
    :linenos:
    :emphasize-lines: 9

.. image:: for/auto_figures/04.svg
  :width: 100
  :alt: TODO ALT TEXT: Resultat fra koden over. En "stjerne" bestående av åtte streker som kommer ut fra samme punkt.
  :class: sphx-glr-script-out

So we can see that the range function creates a sequence of integers up to, but not including, the stopping number (which in this case was 6).
And the ray variable takes on each number in the sequence, one for each "round" in the loop. 

.. sidebar:: Sidetrack: Why do lines 6-9 have an extra indent level?

    Python use indent levels to group lines of code together in code blocks.
    So when we start a loop, for example, by writing ``for ray in range(8)``, we also have to define a code block directly below that contains the lines of code we want to repeat.
    Therefore, everything that should be repeated must be on the same level.
    Below is two examples, one where the turtle moves forwards and backwards 8 times but only rotates once after the loop, and one where the turtle moves forwards 8 times, but only rotates once after the loop. 

    .. image:: for/auto_figures/05.svg
        :width: 180
        :alt: TODO ALT TEXT: Resultat fra koden under. En kort rett strek hvor "skilpadda" er i venstre kant av streken.

    .. collapse:: Kode:

        .. include-turtlethread:: for/05.py
            :linenos:
            :emphasize-lines: 8, 9

    .. image:: for/auto_figures/06.svg
        :width: 180
        :alt: TODO ALT TEXT: Resultat fra koden under. En lengre rett strek hvor "skilpadda" er nesten i høyre kant av streken.

    .. collapse:: Kode:
        
        .. include-turtlethread:: for/06.py
            :linenos:
            :emphasize-lines: 7, 8, 9

        
    .. attention:: 

       Notice that all lines below the line ``with needle.running_stitch(25):`` are indented one extra level.
       This defines a code block of lines that should be sewn with a running stitch, and you can read more about this `here <../auto_examples/gallery_introduction.html>`_.
       
Because ray is a variable, we can also use it in our drawing. If we, for example, want the rays to have different lengths, we can set the length using the ray variable.

.. include-turtlethread:: for/07.py
    :linenos:

.. image:: for/auto_figures/07.svg
    :width: 10
    :alt: TODO ALT TEXT: Resultat fra koden over. Syv veldig små streker med ulik størrelse som danner en "ministjerne". Det er nesten umulig å se detaljer siden strekene er så korte.
    :class: sphx-glr-script-out

This is not what we wanted!
We ended up with a tiny pattern where all the stitches are practically on top of each other.
The reason for this is the ray variable, which only gets values between 0 and 5.
We want our rays to be longer than this!
To get longer rays, we can use the range function.
Range can also decide where the number sequence starts and how big the difference between each number in the sequence should be.
So, if we want the shortest ray to have a length of 50, the longest ray to have a length of 225 and each ray to be 25 longer than the previous, we can write: 

.. include-turtlethread:: for/08.py
    :linenos:
    :emphasize-lines: 5

.. image:: for/auto_figures/08.svg
    :width: 150
    :alt: TODO ALT TEXT: Resultat fra koden over. En stjerne bestående av åtte streker med økende størrelse. Den korteste streken peker til høyre, så øker de i lengde jo lengre man beveger seg med klokka.
    :class: sphx-glr-script-out

Again the interesting line is line 5.
We see that it says ``range(50, 200, 25)``.
This means that the sequence of numbers starts at ``50`` and ends before ``250``, and there is a "jump" of ``25`` steps between each number. 

.. admonition:: Try it yourself:

    Modify the code above so that the smallest ray has a length of 100 steps, the longest has a length of 400 steps, and each ray is 50 steps longer than the last. 

    .. collapse:: Click here to see an example of how the finished code should look. 

        .. include-turtlethread:: for/09.py
            :linenos:
            :emphasize-lines: 5, 8
        
        
        .. image:: for/auto_figures/09.svg
            :width: 90
            :alt: TODO ALT TEXT: Resultat fra koden over. En stjerne bestående av åtte streker med økende størrelse. Den korteste streken peker til høyre, så øker de i lengde jo lengre man beveger seg med klokka.

We can use this technique to make even fancier stars. For example, if we rotate 150 degrees for each loop iteration, we get this figure: 


.. include-turtlethread:: for/10.py
    :linenos:
    :emphasize-lines: 8

.. image:: for/auto_figures/10.svg
    :width: 150
    :alt: TODO ALT TEXT: Resultat fra koden over. En stjerne bestående av åtte streker med ulik størrelse, tilsynelatende uten mønster om hvilke streker som er korte og lange.
    :class: sphx-glr-script-out

.. attention:: 

    If you make a star with a lot of rays, the stitches towards the middle can get too close, which will cause the embroidery machine to struggle and possibly get stuck. 


