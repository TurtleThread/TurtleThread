.. _stitch-types:

Overview of stitch types in TurtleThread
----------------------------------------

TurtleThread currently supports two stitch types: running stitch and jump stitch (zig-zag stitch is under development). 
In this tutorial, we will look at what a stitch type does and what the differences between these two types are. 

No stitches
^^^^^^^^^^^

Let's start by creating a turtle to control our needle and ask the turtle to walk 60 steps forward. 

.. include-turtlethread:: stitch_types/01.py
    :linenos:

What happens when we visualize this?

.. include-turtlethread:: stitch_types/02.py
  :linenos:
  :emphasize-lines: 5

.. image:: stitch_types/manual_code_output/02.svg
  :width: 10
  :alt: Result from the above code.
    An image showing only a triangle that marks the location of the turtle
  :class: sphx-glr-script-out

Here we only see the turtle marker!
This is because we just asked the turtle to move forward. We have yet to ask the turtle to sew with stitches. 
We can see these clearly if we save the embroidery pattern as a text file and look at the file's contents.  

.. include-turtlethread:: stitch_types/03.py
    :linenos:

.. literalinclude:: stitch_types/manual_code_output/pattern_no_stitch.txt

The embroidery pattern doesn't contain any stitches at all!

Running stitch
^^^^^^^^^^^^^^

To get the turtle to sew with stitches while it moves, 
we can use a context manager that decides the stitch type. 
So if we, for example, want a running stitch, we can write. 

.. include-turtlethread:: stitch_types/04.py
    :linenos:
    :emphasize-lines: 4

.. image:: stitch_types/manual_code_output/04.svg
  :width: 100
  :alt: :alt: Result from the above code.
    A horizontal blue line with four short vertical lines with equal distance between them.
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_running_stitch_20.txt

The visualization now shows some short lines across, indicating where the stitches are. 
We can also see from the text file that there are stitches placed at positions (0, 0), (20, 0), (40, 0) and (60, 0). 
So there are 20 steps between each stitch. This 20 step spacing comes from line 4, where we decided the length between stitches by writing ``with needle.running_stitch(20)``. 
If we want the stitches to be 30 steps long instead, we can write:

.. include-turtlethread:: stitch_types/05.py
    :linenos:
    :emphasize-lines: 4

.. image:: stitch_types/manual_code_output/05.svg
  :width: 100
  :alt: Result from the above code.
    A horizontal blue line with three short vertical lines, one at each end and one in the middle. 
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_running_stitch_30.txt

Indentation is important
^^^^^^^^^^^^^^^^^^^^^^^^

Notice that line 5 is indented one step. 
Python uses indenting to group lines of code into one block. 
Suppose we add new lines that are indented equally. 
In that case, they will also belong to the same block, the running stitch block, 
and will be executed with a running stitch. 

.. include-turtlethread:: stitch_types/06.py
    :linenos:
    :emphasize-lines: 6-7

.. image:: stitch_types/manual_code_output/06.svg
  :width: 100
  :alt: Result from the above code.
    A horizontal blue line is followed by a vertical line down, which is half as long as the horizontal line. 
    Every line has short lines across to indicate the position of the stitches
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_angle.txt

We see lines 5-7 belong together in a block under the running stitch context.
We can continue to add as many lines as we want inside the same indent level, and they will be executed with a running stitch seam.  
Here is an example where we have placed a for loop inside the running stitch context:

.. include-turtlethread:: stitch_types/07.py
    :linenos:
    :emphasize-lines: 5-7

.. image:: stitch_types/manual_code_output/07.svg
  :width: 100
  :alt: Result from the above code.
    A blue square with short lines across to mark the stitch positions
  :class: sphx-glr-script-out

If we instead add a line outside the indent level, this line will not be executed with a running stitch seam. 

.. include-turtlethread:: stitch_types/08.py
    :linenos:
    :emphasize-lines: 6-7

.. image:: stitch_types/manual_code_output/08.svg
  :width: 100
  :alt: Result from the above code.
    A horizontal blue line with three short vertical lines, one at each end and one in the middle. 
  :class: sphx-glr-script-out

Jump stitch
^^^^^^^^^^^

If we want to move the needle without creating stitches, we can use the jump stitch. 
For example, the code below shows how we can use a jump stitch to draw two lines with a gap in between. 

.. include-turtlethread:: stitch_types/09.py
    :linenos:
    :emphasize-lines: 8-10

.. image:: stitch_types/manual_code_output/09.svg
  :width: 100
  :alt: Result from the above code.
    A horizontal blue line with three short vertical lines, one at each end and one in the middle, followed by a black cross to indicate that the thread should be cut, a red line ending in a red circle, indicating that the needle should be moved without stitches and finally a new horizontal blue line with three short vertical lines.
  :class: sphx-glr-script-out

.. literalinclude:: stitch_types/manual_code_output/pattern_jump.txt
  :emphasize-lines: 4-5

The visualization above shows that the first blue line ends with a black cross. 
If the embroidery machine you use supports it, 
the thread will be cut here (but not all machines support this). 
If your machine does not support thread cutting, you will have to manually cut it afterwards. 
In the pattern text file, we see the command ``TRIM`` on line 4, 
indicating that the thread should be cut if supported. 
On line 5, we see ``JUMP``, indicating that the needle should move here without creating stitches. 

What is a context manager?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we mentioned at the beginning of this tutorial, 
``with needle.running_stitch(30)`` and ``with needle.jump_stitch()`` are context managers defining which stitch types the turtle should sew with while it moves. 
Context managers in Python are used when we have something that needs a start and end instruction. 
In our case, it is starting and ending a stitch type. 
Behind the scenes 

.. include-turtlethread:: stitch_types/10.py
    :linenos:
    :emphasize-lines: 4

Is the same as

.. include-turtlethread:: stitch_types/11.py
    :linenos:
    :emphasize-lines: 4,6

But it is recommended to use the context manager in most cases. 
This is because it is cleaner and guarantees that you always end the stitch type you started in an orderly way. 