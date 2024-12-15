from pyembroidery import JUMP, STITCH, TRIM
import tkinter as tk
from tkinter.constants import LEFT, RIGHT
from sklearn.cluster import DBSCAN

USE_SPHINX_GALLERY = False


def get_dimensions(stitches):
    x = [s[0] for s in stitches]
    y = [s[1] for s in stitches]
    return max(*x) - min(*x), max(*y) - min(*y)


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


def visualise_pattern(pattern, turtle=None, width=800, height=800, scale=1, speed=6, trace_jump=False, done=True,
                      bye=True):
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

    canvas = screen.getcanvas()
    root = canvas.master

    # Draw grid
    # Vertical thin
    i = 0
    while i < 1000:
        canvas.create_line(i, -1000, i, 1000, width=2, fill="#eeeeee")
        i += 100*scale
    i = 0
    while i > -1000:
        canvas.create_line(i, -1000, i, 1000, width=2, fill="#eeeeee")
        i -= 100 * scale
    # Horizontal thin
    i = 0
    while i < 1000:
        canvas.create_line(-1000, i, 1000, i, width=2, fill="#eeeeee")
        i += 100 * scale
    i = 0
    while i > -1000:
        canvas.create_line(-1000, i, 1000, i, width=2, fill="#eeeeee")
        i -= 100 * scale
    # Vertical thick
    i = 0
    while i < 1000:
        canvas.create_line(i, -1000, i, 1000, width=5, fill="#cccccc")
        i += 500 * scale
    i = 0
    while i > -1000:
        canvas.create_line(i, -1000, i, 1000, width=5, fill="#cccccc")
        i -= 500 * scale
    # Horizontal thick
    i = 0
    while i < 1000:
        canvas.create_line(-1000, i, 1000, i, width=5, fill="#cccccc")
        i += 500 * scale
    i = 0
    while i > -1000:
        canvas.create_line(-1000, i, 1000, i, width=5, fill="#cccccc")
        i -= 500 * scale

    # Write to window directly by getting tkinter object - a bit cursed
    # There probably is a better way to do it

    # Calculate estimated pattern size
    xy = [i / 100 for i in get_dimensions(pattern.stitches)]  # 100 units = 1cm
    # Write pattern size
    tk.Label(
        root,
        text=f"Width: {xy[0]:.2f} cm\nHeight: {xy[1]:.2f} cm",
        justify=LEFT
    ).pack(anchor="s", side="left")

    # Count number of stitches
    stitch_count = sum([1 if command == STITCH else 0 for *_, command in pattern.stitches])
    # Estimate time assuming 600spm
    time = stitch_count / 10
    s = time % 60
    m = time // 60 % 60
    h = time // 3600
    # Write stitch count
    tk.Label(
        root,
        text=f"{stitch_count} stitches in total\n{f'{h}h' if h else ''}{f'{m}m' if m else ''}{s:.1f}s (assuming 600spm)",
        justify=RIGHT
    ).pack(anchor="s", side="right")

    if density(pattern.stitches):
        tk.Label(
            root,
            text=f"WARNING: POTENTIAL HIGH STITCH DENSITY",
            fg="#f00"
        ).pack(side="bottom")

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
            # if stitch is long, limit blank part
            xcur, ycur = turtle.position()
            d = ((xcur - x) ** 2 + (ycur - y) ** 2) ** 0.5  # maybe find a way to avoid fp errors here? prob unnecessary
            blank = min(d/8, 3)
            solid = d - 2*blank

            w = turtle.width()
            turtle.width(3)
            turtle.penup()
            turtle.forward(blank)
            turtle.pendown()
            turtle.forward(solid)
            turtle.penup()
            turtle.forward(blank)
            turtle.pendown()
            turtle.width(w)

        else:
            raise_error = True
            break

    _finish_visualise(done=done, bye=bye)

    if raise_error:
        ValueError(f"Command not supported: {command}")


def density(stitches):
    # Considering that most stitches are of relatively short length,
    # we can estimate the each stitch by some equally spaced apart
    # points, and then find areas with high density.
    # TODO: make algorithm work for longer stitches as well

    # Get sampling points
    points = []
    prevx, prevy = stitches[0][:2]
    for x, y, t in stitches[1:]:
        if t == STITCH:
            points.append(((x+prevx)/4, (y+prevy)/4))
            points.append(((x+prevx)/2, (y+prevy)/2))
            points.append((3*(x+prevx)/4, 3*(y+prevy)/4))

    # Find clusters
    db = DBSCAN(eps=0.5, min_samples=20) # Not hard and fast values
    db.fit(points)
    labels = db.labels_
    return len(set(labels)) > 1
