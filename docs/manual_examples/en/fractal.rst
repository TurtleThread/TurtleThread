Decorating for Christmas with recursive snowflakes
--------------------------------------------------

.. note:: 
    
    This tutorial is a little advanced and assumes that you are already somewhat familiar with functions in Python. 


If we look closer at the "arms" of a snowflake, we may notice that it appears to contain more miniature versions of it self, smaller "arms". When a pattern appears to contain smaller copies of it self we call it a "fractal" or recursive pattern. 

.. figure:: /figures/manual_examples/fractal/SIA-SIA2013-09119.png
    :figwidth: 500

    Fractal snowflake

    A snowflake where each branch of the arms have new branches (`image by Wilson Alwyn Bentley (1865-1931) <https://www.si.edu/object/wilson-bentley-photomicrograph-fernlike-stellar-snowflake-no-1095:siris_arc_403547>`_).

Fraktale mønstre dukker opp mange steder i naturen og kunst. 
Fractal patterns appear many places in both art and nature. 

.. figure:: /figures/manual_examples/fractal/3104423642_31665c5fe4_c.jpg
    :figwidth: 24%

    Fractal cauliflower

    A cauliflower where each flower looks like a small cauliflower (`image by Amber Case (CC-BY-NC) <https://www.flickr.com/photos/caseorganic/3104423642>`_).

.. figure:: /figures/manual_examples/fractal/pexels-jeremy-bishop-14061015.jpg
    :figwidth: 24%

    Fractal tree

    The branches of a tree looks like a tree, and is therefore fractal (`image by Jeremy Bishop <https://www.pexels.com/nb-no/bilde/silhuett-bakke-as-utendors-14061015/>`_).

.. figure:: /figures/manual_examples/fractal/5419811742_9068550c29_c.jpg
    :figwidth: 24%

    Mathematical fractal

    A visualisation of a fractal *Julia set* (`image by Dominic Alves <https://www.flickr.com/photos/dominicspics/5419811742>`_).

.. figure:: /figures/manual_examples/fractal/Kandariya_mahadeva_temple.jpg
    :figwidth: 24%

    The Kandariya Mahadeva Temple

    An image of the Kandariya Mahadeva Temple, which is constructed as a three dimensional fractal (`image by the Wikipedia user Antorjal <https://en.wikipedia.org/wiki/Kandariya_Mahadeva_Temple#/media/File:Kandariya_mahadeva_temple.jpg>`_).


We can draw fractal patterns with code by using recursive functions. 
A recursive function is a function that calls itself.
So what we need to do is to define a function that draws an arm that consists of smaller arms which are drawn by the same function.
This may be a bit confusing, so let's start by creating a simple ``draw_arm`` function that draws a simple snowflake arm.


.. include-turtlethread:: fractal/01.py
    :linenos:
    :emphasize-lines: 5, 9, 14, 19

.. image:: fractal/auto_figures/01.svg
  :width: 180
  :alt: Snowflake arm. A straight line with two branches, one pointing upwards and one pointing downwards.
  :class: sphx-glr-script-out
   

If we call this function, we get a drawing of an arm, and we observe that this arm is built up of four "pieces", where each piece is a line segment.
Instead of a simple line segment, we want each piece to contain a small arm with two new branches. For this, we can replace the call to the ``forward`` function with a call to the ``draw_arm`` function.
Then we get a function which calls itself, also known as a recursive function. 


.. image:: /figures/manual_examples/fractal/recursion_dictionary_en.png
    :width: 400
    :alt: Image of a dictionary, focusing on the word "recursion". The definition is: "See definition of recursion".

.. literalinclude:: fractal/02.py
    :linenos:
    :emphasize-lines: 5, 9, 14, 19

If we run this code, the turtle will never be able to finish the drawing as each branch will consist of an arm with branches where each branch consists of an arm with brances where each branch.... etc. 
This will result in an infinite amount of details that the computer cannot handle, so the program will terminate with a ``RecursionError``.


To ensure that the drawing is eventually completed, we need a variable that keeps track of which "recursion level" we are at. Then we can ensure that we stop after a certain amount of levels: 

.. include-turtlethread:: fractal/03_2.py
    :linenos:
    :emphasize-lines: 3-5, 8, 12, 17, 22, 26

.. image:: fractal/auto_figures/03_2.svg
  :width: 180
  :alt: A snowflake arm. 
    The arm looks like the snowflake arm above, but each straight line has been replaced with a smaller arm.
  :class: sphx-glr-script-out

:Line 3: Here we have added an input argument, recursion_level which keeps track of which level of recursion we are currently at. 
:Lines 4-5: Here we check if we have reached level 0. In that case we should only draw a simple line segment without any branches. This ensures that the drawing is eventually completed. 
:Lines 8, 12, 17 og 22: When we call the ``draw_arm`` function inside the ``draw_arm`` function, we input ``recursion_level - 1`` to indicate that we have "used up" one level of recursion. 
    This ensures that we can keep track of how many levels we have. 
:Line 26: When we call the ``draw_arm`` function outside the function to draw an arm, we can specify how many levels of recursion we want. 

Below are some examples of how the arm looks for different levels of recursion:


**Recursion level 0**

.. image:: fractal/auto_figures/03_0.svg
    :width: 180
    :alt: A straight line

.. collapse:: Kode:

    .. include-turtlethread:: fractal/03_0.py
        :linenos:

**Recursion level 1**

.. image:: fractal/auto_figures/03_1.svg
    :width: 180
    :alt: The same snowflake arm shown in the first code example above. 

.. collapse:: Kode:

    .. include-turtlethread:: fractal/03_1.py
        :linenos:

**Recursion level 2**

.. image:: fractal/auto_figures/03_2.svg
    :width: 180
    :alt: A snowflake arm
        The arm looks like the snowflake arm above, but each straight line has been replaced with a smaller arm.

.. collapse:: Kode:

    .. include-turtlethread:: fractal/03_2.py
        :linenos:


.. admonition:: Try it yourself:
    
    * Update the code to draw snowflake arms with recursion levels 3 and 4.

    .. collapse:: Click here to see the snowflake arm and the code for recursion level 3:

        .. image:: fractal/auto_figures/03_3.svg
            :width: 180
            :alt: A snowflake arm
                The arm looks like the snowflake arm above, but each straight line has been replaced with a smaller arm.
                This process is repeated twice.

        .. include-turtlethread:: fractal/03_3.py
            :linenos:

    
    .. collapse:: Klikk her for å se snøfnugg-armen og koden for rekursjonsnivå 4:

        .. image:: fractal/auto_figures/03_4.svg
            :width: 180
            :alt: A snowflake arm
                The arm looks like the snowflake arm above, but each straight line has been replaced with a smaller arm.
                This process is repeated three times.

        .. include-turtlethread:: fractal/03_4.py
            :linenos:


Now that we have code to draw a snowflake arm, we can use repetition to draw a complete snowflake: 

.. include-turtlethread:: fractal/04.py
    :linenos:
    :emphasize-lines: 26, 28-29

.. image:: fractal/auto_figures/04.svg
    :width: 360
    :alt: A snowflake where each arm has recursion level 2.

.. admonition:: Try it yourself:
    
    * Run the code and see what you get. 
    * Update the code, so the branches point at a different angle (e.g. 60 degrees).
    * Create a modified version of the code where each arm has two sets of branches. Below is a visualisation of how this can look. 

    .. image:: fractal/auto_figures/04.svg
        :width: 180
        :alt: A snowflake arm with two sets of branches. 
    
    .. collapse:: Click here to see an example of how the finished code can look 

        .. include-turtlethread:: fractal/04.py
            :linenos:


    * Create your own fractal! Below is a gallery of examples:

Example fractals
~~~~~~~~~~~~~~~~

**Example fractal 1**

.. image:: fractal/auto_figures/gallery01_1.svg
    :width: 180
    :alt: A different type of fractal snowflake called the "Koch snowflake".
    :class: randomness-gallery-arm

.. image:: fractal/auto_figures/gallery01_2.svg
    :width: 180
    :alt: A different type of fractal snowflake called the "Koch snowflake".
    :class: randomness-gallery-arm

.. collapse:: Code for recursion level 1
    :class: randomness-gallery-code

    .. include-turtlethread:: fractal/gallery01_1.py
        :linenos:

.. collapse:: Code for recursion level 2
    :class: randomness-gallery-code

    .. include-turtlethread:: fractal/gallery01_2.py
        :linenos:

**Example fractal 2**

.. image:: fractal/auto_figures/gallery02_1.svg
    :height: 180
    :alt: A fractal tree.
    :class: randomness-gallery-arm

.. image:: fractal/auto_figures/gallery02_3.svg
    :height: 180
    :alt: A fractal tree.
    :class: randomness-gallery-arm

.. collapse:: Code for recursion level 1
    :class: randomness-gallery-code

    .. include-turtlethread:: fractal/gallery02_1.py
        :linenos:

.. collapse:: Code for recursion level 3
    :class: randomness-gallery-code

    .. include-turtlethread:: fractal/gallery02_3.py
        :linenos:

**Example fractal 3**

.. image:: fractal/auto_figures/gallery03_2.svg
    :width: 180
    :alt: A fractal snowflake with two different arm types, one for even recursion levels and one for odd recursion levels.
    :class: randomness-gallery-arm

.. image:: fractal/auto_figures/gallery03_3.svg
    :width: 180
    :alt: A fractal snowflake with two different arm types, one for even recursion levels and one for odd recursion levels.
    :class: randomness-gallery-arm

.. collapse:: Code for recursion level 2
    :class: randomness-gallery-code

    .. include-turtlethread:: fractal/gallery03_2.py
        :linenos:

.. collapse:: Code for recursion level 3
    :class: randomness-gallery-code

    .. include-turtlethread:: fractal/gallery03_3.py
        :linenos: