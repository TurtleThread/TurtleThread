.. _christmas-randomness:

Christmas decorations, starry nights, and randomness
----------------------------------------------------

.. image::  /../../_static/figures/manual_examples/randomness/ordered_starscape.svg
    :width: 49.5%
    :alt: A simple uniform starry sky.

.. image::  /../../_static/figures/manual_examples/randomness/random_starscape.svg
    :width: 49.5%
    :alt: A  starry sky with randomly placed stars.

Which one of the starry skies above looks the most "natural"?
When we create art with programming, it is easy to end up with very ordered and perfect-looking images.
This can lead to gorgeous patterns, but nature is not perfectly ordered, so it can also look slightly "artificial".
A trick to include a little bit of nature's "not quite perfect"-ness into our art is to use randomness.
Adding randomness is a technique that is commonly found in art, game design, animation and music. 


.. figure:: /../../_static/figures/manual_examples/randomness/10print.svg
    :figwidth: 24%

    Art

    Generative art, variation of 10print


.. figure:: /../../_static/figures/manual_examples/randomness/600px-Tiling_procedural_textures.jpg
    :figwidth: 24%

    Procedurally generated textures for game design

    Illustration of procedurally generated textures (`illustrasjon by Drummyfish <https://en.wikipedia.org/wiki/File:Tiling_procedural_textures.jpg>`_)


.. figure:: /../../_static/figures/manual_examples/randomness/Terragen.jpg
    :figwidth: 24%

    Procedural landscape

    Procedurally generated landscape (`illustration by Levyznin <https://en.wikipedia.org/wiki/File:Terragen.jpg>`_)


.. figure:: /../../_static/figures/manual_examples/randomness/5612345200_a45d40bccb_c.jpg
    :figwidth: 24%

    Music

    Photograph of a modular synthesizer. These instruments can often play sequences of sounds in random order. (`Image by Muff on Flickr (CC-BY 2.0) <https://www.flickr.com/photos/61547250@N02/5612345200>`_)

Randomness with Python
^^^^^^^^^^^^^^^^^^^^^^

Below we se an example of the type of embroidery we will make in this tutorial.

.. image:: /../../_static/figures/manual_examples/randomness/embroidered_random_stars.jpg
    :width: 400
    :alt: An image of a random embroidered starscape.

Let's start by looking at how to generate random numbers in Python. Below is some code to print a random number to the terminal. 

.. include-turtlethread:: randomness/01.py
    :linenos:
    :emphasize-lines: 1,3

:Line 1: Imports the ``random`` library, which we can use to draw random numbers.
:Line 3: Uses the ``random.randint``-function to draw a random number between ``1`` and ``6`` (including endpoints) and stores this random number in the ``random_number`` variable. 

.. admonition:: Try it yourself

    * Run the code several times. Do you get a different number?
    * Modify the code so that it instead prints a random number between 50 and 100
    * Run the code several times again. Do you get different numbers now compared to before?

We can use this to make our embroidery patterns more interesting.
The code below embroiders a simple star:

.. include-turtlethread:: randomness/02.py
    :linenos:

.. image:: randomness/manual_code_output/02.svg
    :width: 180
    :alt: Result from the code above. A simple star with six rays.
    :class: sphx-glr-script-out


To make this star look a little more "natural" and interesting, we can apply randomness to the length of the rays. 


.. include-turtlethread:: randomness/03.py
    :linenos:
    :emphasize-lines: 7
    
.. image:: randomness/manual_code_output/03.svg
    :width: 180
    :alt: Result from the code above. A simple star with six rays with slightly varying length.
    :class: sphx-glr-script-out

:Line 7: draws a random number between ``80`` and ``120`` and stores it in the ``ray_length`` variable.

We can see that the star now looks a little more random and, therefore, a little more natural. 

.. admonition:: Try it yourself:

    * Modify the code, so the ray length is between 25 and 125 instead of 80 and 120. How does the look of the star change?
    * Modify the code, so the number of rays in the star is also random. (HINT: the angle between each ray must be ``360 / number_of_rays``)
    
    .. collapse:: Click here to see an example of how the finished code should look:

        .. include-turtlethread:: randomness/04.py
            :linenos:
            :emphasize-lines: 6-8
        
        .. image:: randomness/manual_code_output/04.svg
            :width: 180
            :alt: Result from the code above. A simple star with a random number of rays and random length on each ray.
            :class: sphx-glr-script-out


.. attention:: 

    Make sure your code matches the finished code above before you proceed.

So, we have created one random star, but we can kick it up a notch by drawing multiple stars randomly placed in the sky.
We can, for example, use the goto command and let the needle move to a random position on the fabric for each star.
The code below draws a starry sky with four random stars randomly placed in the sky.

.. include-turtlethread:: randomness/05.py
    :linenos:
    :emphasize-lines: 6-10
    
.. image:: randomness/manual_code_output/05.svg
    :width: 360
    :alt: Result from the code above. 
        Four stars randomly placed.
        Each star has a random number of rays, each with a random length.
        There is a seam between each star.
    :class: sphx-glr-script-out

:Line 6: Defines a number_of_stars variable that decides how many stars we want to draw
:Line 7: Starts the loop we will use to draw multiple stars
:Lines 8-9: Draws random coordinates between -250 and 250 for each star
:Line 10: Moves the needle to a random position before drawing a star

This is a beautiful, random starry sky!
But now we also embroider a line between each star, which gives a cool effect that can look like constellations.
However, if we don't want these lines, we can use jump stitches to tell the needle to move without stitches between each star. 

.. include-turtlethread:: randomness/06.py
    :linenos:
    :emphasize-lines: 6-7,10,13

    
.. image:: randomness/manual_code_output/06.svg
    :width: 360
    :alt: Result from the code above.
        Four stars randomly placed.
        Each star has a random number of rays, each with a random length.
        There is a seam between each star.
        The stars are now connected with a red line that symbolises that the needle should "jump over" this stretch.
        There is also a black cross in the start of each red line that symbolises that the thread should be cut and a red circle at the end that symbolises the end of a jump stitch.
    :class: sphx-glr-script-out

:Lines 6-7: The loop that iterates over the stars is moved outside the code block that defines stitch type.
    We move the loop to allow for different stitch types when embroidering a star and moving the needle between stars.  
:Line 10: Instructs the needle to move without creating any stitches.
    If the embroidery machine supports it, the thread will be cut (if some stitches have already been embroidered so far).
:Line 13: Starts the code block where we embroider each star with a running stitch. 

.. admonition:: Try it yourself:

    Modify the code to create a random number of stars.

    
    .. collapse:: Click here to see an example of how the finished code should look:

        .. include-turtlethread:: randomness/07.py
            :linenos:
            :emphasize-lines: 6
            
        .. image:: randomness/manual_code_output/07.svg
            :width: 360
            :alt: Result from the code above.
                A random number of stars randomly placed.
                Each star has a random number of rays, each with a random length.
                There is a seam between each star.
                The stars are now connected with a red line that symbolises that the needle should "jump over" this stretch.
                There is also a black cross in the start of each red line that symbolises that the thread should be cut and a red circle at the end that symbolises the end of a jump stitch.
            :class: sphx-glr-script-out

.. image:: /../../_static/figures/manual_examples/randomness/embroidered_random_stars_action.jpg
    :width: 400
    :alt: An image of the embroidery machine while it embroiders a random starscape.

.. attention::

    For this example, we use the randint function from the random library.
    This function draws random numbers that can include the endpoints.
    However, if we use the randint function from ``numpy.random`` or ``pylab``, we would omit the second endpoints.
    For example, ``random.randint(1, 6)`` draws one of these numbers\: 1, 2, 3, 4, 5 or 6, while ``numpy.random.randint(1, 6)`` and ``pylab.randint(1, 6)`` draws one of these numbers\: 1, 2, 3, 4 or 5. 


.. admonition:: Try it yourself:

    * Create your own embroidery pattern that uses randomness. Below is a gallery of that you can take inspiration from.


Example patterns with randomness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Example 1**

.. image:: randomness/manual_code_output/gallery01.svg
    :width: 180
    :alt: A sort of spiral where each line has a random but increasing length.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: randomness/gallery01.py
        :linenos:

**Example 2**

.. image:: randomness/manual_code_output/gallery02.svg
    :width: 180
    :alt: Randomly placed circles with a line connecting them.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: randomness/gallery02.py
        :linenos:

**Example 3**

.. image:: randomness/manual_code_output/gallery03.svg
    :width: 180
    :alt: A snow flake with arms that have random length and a random number of branches
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: randomness/gallery03.py
        :linenos:

**Example 4**

.. image:: randomness/manual_code_output/gallery04.svg
    :width: 180
    :alt: A christmas tree where the length and angle of the branches have some randomness.
    :class: randomness-gallery-arm


.. collapse:: Kode
    :class: randomness-gallery-code

    .. include-turtlethread:: randomness/gallery04.py
        :linenos: