.. _en-snowflake:

Christmas decoration, snowflakes and rotational symmetry
--------------------------------------------------------

This guide will show you how to decorate for Christmas with Python-embroidered ornaments. The image below shows an example of the decorations we will create through turtle programming.

.. note:::

    This guide assumes that you have already installed turtlethread. If this isn't the case, :ref:`click here for instructions<installation>`. 

A classic choice of motive when decorating Christmas ornaments is a snowflake. What is it about the appearance of snowflakes that makes them so decorative?

.. figure:: /../../_static/figures/manual_examples/snowflake/SIA-SIA2013-09130.jpg
    :figwidth: 50%

    Snøfnugg (`image av Wilson Alwyn Bentley (1865-1931) <https://www.si.edu/object/wilson-bentley-photomicrograph-stellar-snowflake-no-990:siris_arc_308076>`_).

If we inspect the crystal closer, we can see that symmetry is one of its key features. Precisely, we can see that it has *rotational symmetry*, which means that it looks the same (except for small “flaws”) when we rotate it. Rotational symmetry is decorative and efficient and is commonly found in nature, mathematics, design, and art. 

.. figure:: /../../_static/figures/manual_examples/snowflake/pexels-julia-volk-7293094.jpg
    :figwidth: 24%

    Nature

    Starfish (`image by Julia Volk <https://www.pexels.com/photo/red-starfish-on-sandy-bottom-of-clear-sea-7293094/>`_).

.. figure:: /../../_static/figures/manual_examples/snowflake/3-7_kisrhombille.svg
    :figwidth: 24%

    Mathematics

    Illustration of a mathematical concept (`illustration by Parcly Taxel <https://commons.wikimedia.org/wiki/File:3-7_kisrhombille.svg>`_)

.. figure:: /../../_static/figures/manual_examples/snowflake/pexels-andreea-ch-1040895.jpg
    :figwidth: 24%

    Art

    A room decorated with colourful tiles (`image by Andreea Ch <https://www.pexels.com/photo/room-with-multicolored-wall-tiles-1040895/>`_)

.. figure:: /../../_static/figures/manual_examples/snowflake/pexels-humphrey-muleba-2271568.jpg
    :figwidth: 24%

    Technology

    Drone (`image by Humphrey Muleba <https://www.pexels.com/photo/person-holding-gray-and-black-quadcopter-drone-2271568/>`_)


Decorate for Christmas with Python-embroidered snow crystals!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Embroider a line
~~~~~~~~~~~~~~~~

Start by copying the code below into your code editor and run it. What image is drawn on the screen?

.. include-turtlethread:: snowflake/01.py
    :linenos:

.. image:: snowflake/manual_code_output/01.svg
    :width: 100
    :alt: Result from the code above.
        A horisontal blue line with three short vertical lines, one on end of the horisontal line and one in the middle.
    :class: sphx-glr-script-out

Let's go through the code line for line:

:Line 1: Imports ``Turtle`` from the ``turtlethread`` library. This can be thought of as asking Python to go in the tool shed  (``turtlethread``), collect the tool (``Turtle``) we need, and place it on our workbench.
:Line 3: Uses the ``Turtle`` command to create a ``Turtle`` object and save it in a variable named ``needle``. This is what we will use for embroidery.
:Line 4: Tells what type of stitch we will use. To read more about different stitches in turtlethread, click here TODO MORE ABOUT STITCHES. 
:Line 5: Tell the needle to move 100 steps forward. Notice that this code is indented one level under the ``with needle.running_stitch(50):``, meaning that the needle will create stitches as it moves.
:Line 7: Calls the needles ``visualise`` method. This method uses ``turtle`` to draw a visualisation of how the embroidery will look and is a nice way to see if your pattern looks right before you try to embroider it onto fabric. 
:Lines 3 and 6: Are empty. Empty lines are used to make the code cleaner and easier to read, but is ignored by the program and removing them has no effect on the output. 


.. admonition:: Try it yourself:

    * Modify the code to use stitches that are 30 steps in length per stitch. Rerun the program, can you tell the difference?
    * Modify the code to make the needle move 90 steps forward instead of 100 steps

    .. collapse:: Click here to see how the finished code should look:

        .. include-turtlethread:: snowflake/02.py
            :linenos:
        
        
        .. image:: snowflake/manual_code_output/02.svg
            :width: 90
            :alt: Result from the code above.
                A horisontal blue line with four short vertical lines with equal spacing between each of them.
            :class: sphx-glr-script-out

.. attention:: 

    Make sure your code matches the finished code above before you proceed. 

Turn right
~~~~~~~~~~

We want the "arms" of the crystal to have "branches".
For this, we need to rotate the needle, which we can do with the ``right`` command.
The below program draws a branch with a 45-degree rotation and a length of 90 steps: 


.. include-turtlethread:: snowflake/03.py
    :linenos:

.. image:: snowflake/manual_code_output/03.svg
    :width: 154
    :alt: Result from the code above.
        A horisontal blue line and a short diagonal line that starts in the right end of the horisontal line.
        The lines have small lines equally spaced across them.
    :class: sphx-glr-script-out

:Lines 5 and 8: Starts with a # symbol, meaning that these lines contain comments that Python will ignore. Comments like these are used to keep the code organised with short explanations. 
:Line 9: Rotate the turtle 45 degrees to the right. 

.. admonition:: Try it yourself:

    * Run the program and see what's drawn on the screen
    * Modify the code, so the branch is rotated 30 degrees instead of 45
    * Modify the code, so the branch has a length of 60 instead of 90.

    .. collapse:: Klikk her for å se programmet slik det skal være om du har gjort det rett:

        .. include-turtlethread:: snowflake/04.py
            :linenos:

        .. image:: snowflake/manual_code_output/04.svg
            :width: 168
            :alt: Result from the code above.
                A horisontal blue line and a short diagonal line that starts in the right end of the horisontal line.
                The lines have small lines equally spaced across them.
            :class: sphx-glr-script-out

.. attention:: 

    Make sure your code matches the finished code above before you proceed. 


Complete the snowflake arm
~~~~~~~~~~~~~~~~~~~~~~~~~~

After drawing a branch, we must move backwards and rotate back to continue the arm. For this, we can use ``backward`` and ``left``:


.. include-turtlethread:: snowflake/05.py
    :linenos:

.. image:: snowflake/manual_code_output/05.svg
    :width: 180
    :alt: Result from the code above.
        A horisontal blue line and a short downwards facing diagonal line that starts in the middle of the horisontal line.
        The lines have small lines equally spaced across them.
    :class: sphx-glr-script-out


.. admonition:: Prøv selv:

    * Run the program and see what's drawn on the screen
    * Why are the numbers on lines 10 and 11 equal? Is this important? Why/why not?

We'll finish the "arm" by moving backwards and drawing a branch on the other side.
It's important that we end with the needle in the same position and pointing in the same direction as we started: 

.. include-turtlethread:: snowflake/06.py
    :linenos:

.. image:: snowflake/manual_code_output/06.svg
    :width: 180
    :alt: Result from the code above.
        A long horisontal blue line and two diagonal lines that start in the middle of the horisontal line, one pointing downwards and one pointing upwards.
        All three lines have small lines across to represent stitches with equal distance between each stitch.
    :class: sphx-glr-script-out


.. admonition:: Try it yourself

    * Run the code and see what is drawn on the screen. 
    * What does line 19 to 22 do?


.. attention:: 

    Make sure your code matches the finished code above before you proceed.


Use loops to form a snowflake
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we have code to instruct are needle-turtle to embroider one arm of a snowflake.
However, most snowflakes have multiple arms. So, to draw a full flake, we need to repeat these commands multiple times.
For this, we can use a loop.
If you want to read more about loops in Python you can click :ref:`here <for_en>`, but for now you just need to know that we can draw four arms with a for loop like so: 


.. include-turtlethread:: snowflake/07.py
    :linenos:
    :emphasize-lines: 6, 30

.. image:: snowflake/manual_code_output/07.svg
    :width: 360
    :alt: Result from the code above.
        A snowflake with four "arms".
        Each arm is identical to that in the previous image.
    :class: sphx-glr-script-out

.. sidebar:: Sidespor: Hvorfor måtte skilpadda tilbake til start?
    
        Hvis skilpadda ikke hadde gått tilbake til start og pekt i samme retning som den startet, ville vi ikke kunne brukt en løkke for å tegne snøflaket.
        Under er to eksempler, et hvor skilpadda avslutter på feil posisjon og et hvor skilpadda avslutter med feil vinkel.

        .. image:: snowflake/manual_code_output/09.svg
            :width: 180
            :alt: Result from the code above.
                Attempt at drawing a snowflake where we don't return back to start for each arm.

        .. collapse:: Kode:

            .. include-turtlethread:: snowflake/09.py
                :linenos:

        .. image:: snowflake/manual_code_output/10.svg
            :width: 180
            :alt: Result from the code above.
                Attempt at drawing a snowflake where we don't rotate between each arm.
                All arms are embroidered on top of each other so it looks like there is only one arm.

        .. collapse:: Kode:
            
            .. include-turtlethread:: snowflake/10.py
                :linenos:

:Line 6: Starts a for loop and lets Python know that everything in this loop should happen 4 times. Notice that lines 7-20 have been indented an extra level. This tells Python that these lines are inside the loop and should be repeated for each loop repetition. 
:Line 30: Tells the turtle to rotate 90 degrees for each loop repetition. This rotation is necessary so we don't draw all four arms on top of each other. 

.. admonition:: Try it yourself:
    
    * Run the program and see what is drawn on the screen
    * Why is there a 90-degree rotation on line 30? What happens if you change it to 60 instead?
    * Modify the code to draw a snowflake with 6 arms instead of 4. 

    .. collapse:: Click here to see how the finished code should look:

        .. include-turtlethread:: snowflake/08.py
            :linenos:

        .. image:: snowflake/manual_code_output/08.svg
            :width: 360
            :alt: Result from the code above.
                A snoflake with six "arms".
                Otherwise equal to the image above.
            :class: sphx-glr-script-out


.. attention:: 

    Make sure your code matches the finished code above before you proceed. 

Now we have code to draw a complete snowflake!

.. admonition:: Try it yourself:

    Use code to draw your own snowflake with rotational symmetry. Below is a gallery with some examples you can use as a starting point or just for inspiration!

Create an ornament with your snowflake 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create an ornament with the snowflake embroidery you can follow these instructions:

1.	Embroider two snowflakes (either on the same fabric or two different if you want different sides) 
2.	Place the two fabric pieces on top of each other so the embroidery patterns are on top of each other and pointing outwards. 
3.	Sew the pieces together (either by hand or by drawing a circle with turtlethread). Here is a guide for sewing and constructing the ornaments TODO.

Example snowflakes
~~~~~~~~~~~~~~~~~~

**Snowflake 1**

.. image:: snowflake/manual_code_output/gallery01.svg
    :width: 180
    :alt: Two arms of different snowflakes on top of each other, with a 30 degree rotation between the arms. 
        One of the arm-types consists of one long line with three circles of varying size on top of each other at the end.
        The other arm-type consists of a small line with a small circle at the end.
    :class: snowflake-gallery-arm

.. collapse:: Snowflake
    :class: snowflake-gallery-snowflake

    .. image:: snowflake/manual_code_output/gallery01_full.svg
        :width: 360 
        :alt: Two different snowflakes on top of each other, making a snowflake with 12 arms of alternating type. 
            One of the arm-types consists of one long line with three circles of varying size on top of each other at the end.
            The other arm-type consists of a small line with a small circle at the end.


.. collapse:: Code for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery01.py
        :linenos:

.. collapse:: Code for snowflake
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery01_full.py
        :linenos:


**Snowflake 2**

.. image:: snowflake/manual_code_output/gallery02.svg
    :width: 180
    :alt: A right angled triangle whose hypothenus is horizontal.
        The proportion of the triangle's legs to its hypothenus is 3/5 and 4/5.
    :class: snowflake-gallery-arm

.. collapse:: Snowflake
    :class: snowflake-gallery-snowflake

    .. image:: snowflake/manual_code_output/gallery02_full.svg
        :width: 360
        :alt: A snowflake whose six arms are right-angled triangles. It resembles a paper fan.


.. collapse:: Code for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery02.py
        :linenos:

.. collapse:: Code for snowflake
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery02_full.py
        :linenos:


**Snowflake 3**

.. image:: snowflake/manual_code_output/gallery03.svg
    :width: 180
    :alt: Two arms of different snowflakes on top of each other, with a 30 degree rotation between the arms. 
        Both arms resemble those we made in this tutorial but of different sizes.
    :class: snowflake-gallery-arm

.. collapse:: Snowflake
    :class: snowflake-gallery-snowflake

    .. image:: snowflake/manual_code_output/gallery03_full.svg
        :width: 360
        :alt: Two different snowflakes on top of each other, making a snowflake with 12 arms of alternating type. 
            Both snowflakes have arms resemble those we made in this tutorial but of different sizes.


.. collapse:: Code for arm
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery03.py
        :linenos:

.. collapse:: Code for snowflake
    :class: snowflake-gallery-code

    .. include-turtlethread:: snowflake/gallery03_full.py
        :linenos: