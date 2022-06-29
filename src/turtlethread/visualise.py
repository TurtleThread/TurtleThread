from math import atan2

from pyembroidery import JUMP, STITCH, TRIM, EmbPattern, write


USE_SPHINX_GALLERY = False


def centered_dot(turtle, diameter):
    pensize = turtle.pensize()
    turtle.pensize(diameter)
    turtle.goto(turtle.position())
    turtle.pensize(pensize)


def centered_cross(turtle, length):
    r = length/2
    x, y = turtle.position()
    turtle.goto(x + r, y + r)
    turtle.goto(x - r, y - r)
    turtle.goto(x, y)
    turtle.goto(x + r, y - r)
    turtle.goto(x - r, y + r)
    turtle.goto(x, y)

def centered_line(turtle, length):
    r = length/2
    tr = turtle._tracer()
    dl = turtle._delay()
    turtle._tracer(0, 0)
    x, y = turtle.position()
    turtle.right(90)
    turtle.forward(r)
    turtle.penup()
    turtle.backward(r)
    turtle.pendown()
    turtle.backward(r)
    turtle.penup()
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle._tracer(tr, dl)


def visualise_pattern(pattern, turtle=None, width=800, height=800, scale=1, done=True, bye=True):
    """Use the builtin ``turtle`` library to visualise an embroidery pattern.

    Parameters
    ----------
    pattern : pyembroidery.EmbPattern
        Embroidery pattern to visualise
    turtle : turtle.Turtle (optional)
        Python turtle object to use for drawing. If not specified, then the default turtle
        is used.
    width : int
        Canvas width
    height : int
        Canvas height
    scale : int
        Factor the embroidery length's are scaled by.
    done : bool
        If True, then ``turtle.done()`` will be called after drawing.
    bye : bool
        If True, then ``turtle.bye()`` will be called after drawing.
    """
    if USE_SPHINX_GALLERY:
        return

    # Lazy import of 'turtle' module just for visualization so that the rest of
    # the library can be used on Python installs where the GUI libraries are not
    # available.
    #
    # (This looks like it would conflict with the 'turtle' variable but it does not)
    from turtle import Turtle, Screen

    if turtle is None:
        # If turtle is None, grab the default turtle and set its speed to fastest
        if Turtle._pen is None:
            Turtle._pen = Turtle()
        turtle = Turtle._pen

        turtle.speed('fastest')
    screen = Screen()
    screen.setup(width, height)

    turtle.penup()
    turtle.goto(pattern.stitches[0][0], pattern.stitches[0][1])
    turtle.pendown()

    raise_error = False
    for x, y, command in pattern.stitches:
        x = scale*x
        y = -scale*y
        if command == JUMP:
            turtle.color("red")
            turtle.goto(x, y)

            speed = turtle.speed()
            turtle.speed('fastest')
            centered_dot(turtle, 25*scale)
            turtle.speed(speed)
        elif command == TRIM:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            turtle.color("black")
            speed = turtle.speed()
            turtle.speed('fastest')
            centered_cross(turtle, 25*scale)
            turtle.speed(speed)
        elif command == STITCH:
            turtle.setheading(turtle.towards(x, y))
            turtle.pendown()
            turtle.color("blue")
            turtle.goto(x, y)
            speed = turtle.speed()
            turtle.speed('fastest')
            centered_line(turtle, 10*scale)
            turtle.speed(speed)
        else:
            raise_error = True
            break

    if done:
        import turtle  # Import turtle only here to avoid cluttering module namespace
        turtle.done()
    if bye:
        import turtle  # Import turtle only here to avoid cluttering module namespace
        turtle.bye()

    if raise_error:
        ValueError(f"Command not supported: {command}")

