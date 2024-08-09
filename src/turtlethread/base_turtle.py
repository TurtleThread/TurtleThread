"""This module contains code from the builtin turtle.py, but without importing TKinter.

We need to do this since we want TurtleThread to work on platforms with Python compiled
without TKinter support. However, we also want to base our Turtle class on the
TNavigator class in the builtin turtle.py.
"""

# Copyright notice from the builtin turtle.py:
#
# turtle.py: a Tkinter based turtle graphics module for Python
# Version 1.1b - 4. 5. 2009
#
# Copyright (C) 2006 - 2010  Gregor Lingl
# email: glingl@aon.at
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
import math


class Vec2D(tuple):
    """A 2 dimensional vector class, used as a helper class
    for implementing turtle graphics.
    May be useful for turtle graphics programs also.
    Derived from tuple, so a vector is a tuple!

    Provides (for a, b vectors, k number):
       a+b vector addition
       a-b vector subtraction
       a*b inner product
       k*a and a*k multiplication with scalar
       |a| absolute value of a
       a.rotate(angle) rotation
    """

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __add__(self, other):
        return Vec2D(self[0] + other[0], self[1] + other[1])

    def __mul__(self, other):
        if isinstance(other, Vec2D):
            return self[0] * other[0] + self[1] * other[1]
        return Vec2D(self[0] * other, self[1] * other)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2D(self[0] * other, self[1] * other)
        return NotImplemented

    def __sub__(self, other):
        return Vec2D(self[0] - other[0], self[1] - other[1])

    def __neg__(self):
        return Vec2D(-self[0], -self[1])

    def __abs__(self):
        return math.hypot(*self)

    def rotate(self, angle):
        """rotate self counterclockwise by angle"""
        perp = Vec2D(-self[1], self[0])
        angle = math.radians(angle)
        c, s = math.cos(angle), math.sin(angle)
        return Vec2D(self[0] * c + perp[0] * s, self[1] * c + perp[1] * s)

    def __getnewargs__(self):
        return (self[0], self[1])

    def __repr__(self):
        return "(%.2f,%.2f)" % self


class TNavigator(object):
    """Navigation part of the RawTurtle.
    Implements methods for turtle movement.
    """

    START_ORIENTATION = {"standard": Vec2D(1.0, 0.0), "world": Vec2D(1.0, 0.0), "logo": Vec2D(0.0, 1.0)}
    DEFAULT_MODE = "standard"
    DEFAULT_ANGLEOFFSET = 0
    DEFAULT_ANGLEORIENT = 1

    def __init__(self, mode=DEFAULT_MODE):
        self._angleOffset = self.DEFAULT_ANGLEOFFSET
        self._angleOrient = self.DEFAULT_ANGLEORIENT
        self._mode = mode
        self.undobuffer = None
        self.degrees()
        self._mode = None
        self._setmode(mode)
        TNavigator.reset(self)

    def reset(self):
        """reset turtle to its initial values

        Will be overwritten by parent class
        """
        self._position = Vec2D(0.0, 0.0)
        self._orient = TNavigator.START_ORIENTATION[self._mode]

    def _setmode(self, mode=None):
        """Set turtle-mode to 'standard', 'world' or 'logo'."""
        if mode is None:
            return self._mode
        if mode not in ["standard", "logo", "world"]:
            return
        self._mode = mode
        if mode in ["standard", "world"]:
            self._angleOffset = 0
            self._angleOrient = 1
        else:  # mode == "logo":
            self._angleOffset = self._fullcircle / 4.0
            self._angleOrient = -1

    def _setDegreesPerAU(self, fullcircle):
        """Helper function for degrees() and radians()"""
        self._fullcircle = fullcircle
        self._degreesPerAU = 360 / fullcircle
        if self._mode == "standard":
            self._angleOffset = 0
        else:
            self._angleOffset = fullcircle / 4.0

    def degrees(self, fullcircle=360.0):
        """Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Default value is
        360 degrees.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> turtle.degrees(400.0)
        >>> turtle.heading()
        100

        """
        self._setDegreesPerAU(fullcircle)

    def radians(self):
        """Set the angle measurement units to radians.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        """
        self._setDegreesPerAU(math.tau)

    def _go(self, distance):
        """move turtle forward by specified distance"""
        ende = self._position + self._orient * distance
        self._goto(ende)

    def _rotate(self, angle):
        """Turn turtle counterclockwise by specified angle if angle > 0."""
        angle *= self._degreesPerAU
        self._orient = self._orient.rotate(angle)

    def _goto(self, end):
        """move turtle to position end."""
        self._position = end

    def forward(self, distance):
        """Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """
        self._go(distance)

    def back(self, distance):
        """Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance, opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """
        self._go(-distance)

    def right(self, angle):
        """Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """
        self._rotate(-angle)

    def left(self, angle):
        """Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """
        self._rotate(angle)

    def pos(self):
        """Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """
        return self._position

    def xcor(self):
        """Return the turtle's x coordinate.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        """
        return self._position[0]

    def ycor(self):
        """Return the turtle's y coordinate
        ---
        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        """
        return self._position[1]

    def goto(self, x, y=None):
        """Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """
        if y is None:
            self._goto(Vec2D(*x))
        else:
            self._goto(Vec2D(x, y))

    def home(self):
        """Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example (for a Turtle instance named turtle):
        >>> turtle.home()
        """
        self.goto(0, 0)
        self.setheading(0)

    def setx(self, x):
        """Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        """
        self._goto(Vec2D(x, self._position[1]))

    def sety(self, y):
        """Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
        """
        self._goto(Vec2D(self._position[0], y))

    def distance(self, x, y=None):
        """Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
        """
        if y is not None:
            pos = Vec2D(x, y)
        if isinstance(x, Vec2D):
            pos = x
        elif isinstance(x, tuple):
            pos = Vec2D(*x)
        elif isinstance(x, TNavigator):
            pos = x._position
        return abs(pos - self._position)

    def towards(self, x, y=None):
        """Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0
        """
        if y is not None:
            pos = Vec2D(x, y)
        if isinstance(x, Vec2D):
            pos = x
        elif isinstance(x, tuple):
            pos = Vec2D(*x)
        elif isinstance(x, TNavigator):
            pos = x._position
        x, y = pos - self._position
        result = round(math.degrees(math.atan2(y, x)), 10) % 360.0
        result /= self._degreesPerAU
        return (self._angleOffset + self._angleOrient * result) % self._fullcircle

    def heading(self):
        """Return the turtle's current heading.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0
        """
        x, y = self._orient
        result = round(math.degrees(math.atan2(y, x)), 10) % 360.0
        result /= self._degreesPerAU
        return (self._angleOffset + self._angleOrient * result) % self._fullcircle

    def setheading(self, to_angle):
        """Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """
        angle = (to_angle - self.heading()) * self._angleOrient
        full = self._fullcircle
        angle = (angle + full / 2.0) % full - full / 2.0
        self._rotate(angle)

    def circle(self, radius, extent=None, steps=None):
        """Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example (for a Turtle instance named turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle
        """
        if self.undobuffer:
            self.undobuffer.push(["seq"])
            self.undobuffer.cumulate = True
        speed = self.speed()
        if extent is None:
            extent = self._fullcircle
        if steps is None:
            frac = abs(extent) / self._fullcircle
            steps = 1 + int(min(11 + abs(radius) / 6.0, 59.0) * frac)
        w = 1.0 * extent / steps
        w2 = 0.5 * w
        l = 2.0 * radius * math.sin(math.radians(w2) * self._degreesPerAU)
        if radius < 0:
            l, w, w2 = -l, -w, -w2
        tr = self._tracer()
        dl = self._delay()
        if speed == 0:
            self._tracer(0, 0)
        else:
            self.speed(0)
        self._rotate(w2)
        for i in range(steps):
            self.speed(speed)
            self._go(l)
            self.speed(0)
            self._rotate(w)
        self._rotate(-w2)
        if speed == 0:
            self._tracer(tr, dl)
        self.speed(speed)
        if self.undobuffer:
            self.undobuffer.cumulate = False

    ## three dummy methods to be implemented by child class:

    def speed(self, s=0):
        """dummy method - to be overwritten by child class"""

    def _tracer(self, a=None, b=None):
        """dummy method - to be overwritten by child class"""

    def _delay(self, n=None):
        """dummy method - to be overwritten by child class"""

    fd = forward
    bk = back
    backward = back
    rt = right
    lt = left
    position = pos
    setpos = goto
    setposition = goto
    seth = setheading
