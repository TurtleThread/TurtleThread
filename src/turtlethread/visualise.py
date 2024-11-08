from pyembroidery import JUMP, STITCH, TRIM

USE_SPHINX_GALLERY = False


def centered_dot(turtle, diameter):
    speed = turtle.speed()
    turtle.speed(0)
    pensize = turtle.pensize()
    turtle.pensize(diameter)
    turtle.goto(turtle.position())
    turtle.pensize(pensize)
    turtle.speed(speed)


def centered_cross(turtle, length):
    speed = turtle.speed()
    turtle.speed(0)
    r = length / 2
    x, y = turtle.position()
    turtle.goto(x + r, y + r)
    turtle.goto(x - r, y - r)
    turtle.goto(x, y)
    turtle.goto(x + r, y - r)
    turtle.goto(x - r, y + r)
    turtle.goto(x, y)
    turtle.speed(speed)


def centered_line(turtle, length):
    speed = turtle.speed()
    turtle.speed(0)
    r = length / 2
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
    turtle.speed(speed)


def _finish_visualise(done, bye):
    import turtle  # Import turtle only here to avoid cluttering module namespace

    if done:
        try:
            turtle.done()
        except turtle.Terminator:
            pass
    if bye:
        try:
            turtle.bye()
        except turtle.Terminator:
            pass


def visualise_pattern(pattern, turtle=None, width=800, height=800, scale=1, speed=6, trace_jump=False, done=True, bye=True):
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
    speed : int
        Speed that the turtle object moves at.
    trace_jump : bool
        If True, then draw a grey line connecting the origin and destination of jumps.
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
    from turtle import Screen, Turtle

    if turtle is None:
        # If turtle is None, grab the default turtle and set its speed to fastest
        if Turtle._pen is None:
            Turtle._pen = Turtle()
        turtle = Turtle._pen

    turtle.speed(speed)

    screen = Screen()
    screen.setup(width, height)

    if len(pattern.stitches) == 0:
        _finish_visualise(done=done, bye=bye)
        return

    turtle.penup()
    turtle.goto(pattern.stitches[0][0], pattern.stitches[0][1])
    turtle.pendown()

    raise_error = False
    for x, y, command in pattern.stitches:
        x = scale * x
        y = scale * y
        if command == JUMP:
            # turtle.color("red")
            turtle.color(0.8, 0.8, 0.8)
            if not trace_jump: turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            centered_dot(turtle, 10 * scale)
        elif command == TRIM:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            # turtle.color("black")
            turtle.color(0.8, 0.8, 0.8)
            centered_cross(turtle, 10 * scale)
        elif command == STITCH:
            turtle.setheading(turtle.towards(x, y))
            turtle.color("blue")

            # 12.5% 75%  12.5%
            # blank line blank
            xcur, ycur = turtle.position()
            d = ((xcur-x)**2 + (ycur-y)**2)**0.5 # TODO: find a way to avoid fp errors here

            turtle.penup()
            turtle.forward(d/8)
            turtle.pendown()
            turtle.forward(d/4*3)
            turtle.penup()
            turtle.forward(d/8)
            turtle.pendown()

        else:
            raise_error = True
            break

    _finish_visualise(done=done, bye=bye)

    if raise_error:
        ValueError(f"Command not supported: {command}")
