"""
Your first turtle embroidery
============================

We will now make our first turtle embroidery.
We start by importing TurtleThread (make sure that it is `installed <../installation.html>`_).
"""


import turtlethread

# %%
# Next, we create a turtle object, which we'll use to draw with

needle = turtlethread.Turtle()

# %%
# Now we have everything we need to start making patterns. Let's start with a line.
# To draw a line, we use ``forward`` and how far we want the turtle to move (for example 300 steps).

needle = turtlethread.Turtle()
needle.forward(300)

# %%
# This code moves the turtle 100 steps, but it doesn't make any stitches.
# To make the turtle start stitching while it is moving, we need to use a stitch-block.
# The simplest form of stitch-block is one named ``running_stitch``. In a running stitch block,
# we embroider in a straight line with a set distance between each stitch.

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    needle.forward(300)

# %%
# Now, we have made code that moves the turtle 300 steps forward, with one stitch after every 30-th step.
# This is equivalent to stitching every third millimeter. Let's see how this looks, and to do so, we can use
# the ``visualise``-function, which uses the builtin ``turtle``-library to draw our embroidery.

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    needle.forward(300)
needle.visualise()

# %%
# .. image:: ../figures/introduction_1.png

# %%
# Now, we have a straight line, and to change direction, we can use the ``right``-command, and tell the turtle
# how many degrees it should turn to the right (for example 90 degrees).

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    needle.forward(300)
    needle.right(90)
    needle.forward(300)

needle.visualise()

# %%
# .. image:: ../figures/introduction_2.png


# %%
# With a for-loop, we can repeat this four times to get a square:

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    for side in range(4):
        needle.forward(300)
        needle.right(90)

needle.visualise()

# %%
# .. image:: ../figures/introduction_3.png

# %%
# And if we use another loop again to draw the square eight times, we'll get a pretty flower:

needle = turtlethread.Turtle()
with needle.running_stitch(30):
    for kronblad in range(8):
        for side in range(4):
            needle.forward(300)
            needle.right(90)
        needle.right(45)

needle.visualise()

# %%
# .. image:: ../figures/introduction_4.png

# # %%
# It can often be smart to define some key variables to use in our program. One such variable can be
# the number of petals our flower has. Let's make that petal variable and name it ``antall_kronblader``,
# which means number of petals in Norwegian.


needle = turtlethread.Turtle()
antall_kronblader = 8

with needle.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            needle.forward(300)
            needle.right(90)
        needle.right(360 / antall_kronblader)

# %%
# Try to modify the code and change the number of petals

# %%
# Now, we have a nice pattern that we can save as a PNG or SVG file

needle = turtlethread.Turtle()
antall_kronblader = 8

with needle.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            needle.forward(300)
            needle.right(90)
        needle.right(360 / antall_kronblader)

needle.save("firkantblomst.png")
needle.save("firkantblomst.svg")


# %%
# Or, we can save it as a DST-file to use it with an embroidery machine.

needle = turtlethread.Turtle()
antall_kronblader = 8

with needle.running_stitch(30):
    for kronblad in range(antall_kronblader):
        for side in range(4):
            needle.forward(300)
            needle.right(90)
        needle.right(360 / antall_kronblader)

needle.save("firkantblomst.dst")
