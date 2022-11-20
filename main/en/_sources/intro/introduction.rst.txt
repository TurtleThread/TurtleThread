.. _introduction:

Your first turtle embroidery
============================

We will now make our first turtle embroidery.
We start by importing TurtleThread (make sure that it is `installed <../installation.html>`_).

.. include-turtlethread:: introduction/01.py
    :linenos:
    :lines: 1

Next, we create a turtle object, which we'll use to draw with

.. include-turtlethread:: introduction/01.py
    :linenos:
    :lines: 1-3
    :emphasize-lines: 3

Now we have everything we need to start making patterns. Let's start with a line.
To draw a line, we use ``forward`` and how far we want the turtle to move (for example 300 steps).

.. include-turtlethread:: introduction/01.py
    :linenos:
    :emphasize-lines: 4

This code moves the turtle 100 steps, but it doesn't make any stitches.
To make the turtle start stitching while it is moving, we need to use a stitch-block.

Using a stitch type to create a seam
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simplest form of stitch-block is one named ``running_stitch`` (See :ref:`stitch-types`). In a running stitch block,
we embroider in a straight line with a set distance between each stitch.

.. include-turtlethread:: introduction/02.py
    :linenos:
    :lines: 1-5
    :emphasize-lines: 4

Now, we have made code that moves the turtle 300 steps forward, with one stitch after every 30-th step.
This is equivalent to stitching every third millimeter. Let's see how this looks, and to do so, we can use
the ``visualise``-function, which uses the builtin ``turtle``-library to draw our embroidery.

.. include-turtlethread:: introduction/02.py
    :linenos:
    :emphasize-lines: 6

.. image:: introduction/manual_code_output/02.svg
  :width: 180
  :alt: A straight line with short vertical lines across that indicate where stitches are placed.
  :class: sphx-glr-script-out

Now, we have a straight line, and to change direction, we can use the ``right``-command, and tell the turtle
how many degrees it should turn to the right (for example 90 degrees).

.. include-turtlethread:: introduction/03.py
    :linenos:
    :emphasize-lines: 6-7

.. image:: introduction/manual_code_output/03.svg
  :width: 180
  :alt: A straight hoizontal line followed by a vertical line of the same size. Both lines have short lines across that indicate where stitches are placed.
  :class: sphx-glr-script-out

With a for-loop, we can repeat this four times to get a square:

.. include-turtlethread:: introduction/04.py
    :linenos:
    :emphasize-lines: 5-7
    
.. image:: introduction/manual_code_output/04.svg
  :width: 180
  :alt: A straight large square with short lines across each border that indicate where stitches are placed.
  :class: sphx-glr-script-out

And if we use another loop again to draw the square eight times, we'll get a pretty flower:

.. include-turtlethread:: introduction/05.py
    :emphasize-lines: 5
    :linenos:

.. image:: introduction/manual_code_output/05.svg
  :width: 180
  :alt: Eight squares placed on top of each other to form what looks like a flower.
  :class: sphx-glr-script-out

It can often be smart to define some key variables to use in our program. One such variable can be
the number of petals our flower has. Let's make that petal variable and name it ``num_petals``.

.. include-turtlethread:: introduction/06.py
    :emphasize-lines: 5, 7
    :linenos:
    :lines: 1-13
    
.. image:: introduction/manual_code_output/06.svg
  :width: 180
  :alt: Eight squares placed on top of each other to form what looks like a flower.
  :class: sphx-glr-script-out


.. admonition:: Try it yourself:

    * Try to modify the code and change the number of petals to get a figure like the one below:

    .. image:: introduction/manual_code_output/07.svg
        :width: 180
        :alt: Ten squares placed on top of each other to form what looks like a flower.
        :class: sphx-glr-script-out

    .. collapse:: Click here to see an example of how the finished code can look:
    
        .. include-turtlethread:: introduction/07.py
            :linenos:
            :lines: 1-13
            :emphasize-lines: 5


Saving the pattern
^^^^^^^^^^^^^^^^^^

Now, we have a nice pattern that we can save as a PNG or SVG file

.. include-turtlethread:: introduction/06.py
    :linenos:
    :lines: 1-15
    :emphasize-lines: 14-15

Below is the ``flower.svg`` file that we just created:

.. image:: introduction/manual_code_output/flower.svg
    :width: 180
    :alt: Eight squares placed on top of each other to form what looks like a flower.

Or, we can save it as a DST-file to use it with an embroidery machine.

.. include-turtlethread:: introduction/06.py
    :linenos:
    :emphasize-lines: 16

.. image:: ../../../_static/figures/firkantblomst_sydd.png
  :width: 400
  :alt: Example generated with TurtleThread.