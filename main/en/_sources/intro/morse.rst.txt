.. _morse:

Embroidering a message with morse code
---------------------------------------

In this example, we'll look at how we can translate messages to morse code and how we can make an embroidery pattern from these messages.

Drawing morse code
^^^^^^^^^^^^^^^^^^

We start by importing ``Turtle`` from ``turtlethread``

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 1

The next step is to make code thad draws morse code with a turtle object.
We start by defining how we draw a dot and a dash. 
What we know about morse code is:

- A dot lasts for one time unit
- A dash lasts for three time units
- There is three time units between each sign
- There is seven time units between each word

Based on this, we can draw dots and dashes with ``turtlethread``.
There are many ways we could do this, but we've selected the following:

.. image:: ../../../_static/figures/morse/morse_en.svg

Let's start by making three functions: one to draw a dash, one to draw a dot and one which takes a morse symbol (dot, dash or space) and draws it.

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 4-34

Now we have code that can draw each sign in a morse code, but we also want code to draw a whole message.

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 36-48

Let's try this out by drawing SOS (``... --- ...``).

.. include-turtlethread:: morse/01.py
    :linenos:
    :lines: 50-54

.. image:: morse/manual_code_output/sos.svg
  :width: 400
  :alt: SOS skrevet med morsekode.
  :class: sphx-glr-script-out

Converting text to morse code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next step is to make code that makes text into morse code.
To do this, we use a dictionary that maps letters and symbols to morse code.

.. include-turtlethread:: morse/02.py
    :linenos:
    :lines: 50-66

Next, we create a function that takes a text string as input and transforms it to morse code.

.. include-turtlethread:: morse/03.py
    :linenos:
    :lines: 69-76

Drawing text as morse code
^^^^^^^^^^^^^^^^^^^^^^^^^^

We have now managed to write "Hello morse" with morse code!
Let's use the ``draw_morse_code`` function to draw this message.

.. include-turtlethread:: morse/04.py
    :linenos:
    :lines: 76-81

.. image:: morse/manual_code_output/hello_morse.svg
    :width: 600
    :alt: The text "hello_morse" as morse code.
    :class: sphx-glr-script-out

Now we have a nice little message.
Let's end it all by making a function that takes a text string as input and uses a turtle object to draw the morse code that represents the string.

.. include-turtlethread:: morse/05.py
    :linenos:
    :lines: 76-85

.. image:: morse/manual_code_output/hello_world.svg
    :width: 600
    :alt: The text "hello world" as morse code.
    :class: sphx-glr-script-out
