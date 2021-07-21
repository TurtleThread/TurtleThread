from math import atan2
from turtle import Turtle, Screen

from pyembroidery import JUMP, STITCH, TRIM, EmbPattern, write


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


def visualise_pattern(pattern, turtle=None, width=800, height=800, scale=0.2):
    if turtle is None:
        turtle = Turtle()
        turtle.speed('fastest')
    screen = Screen()
    screen.setup(width, height)

    for x, y, command in pattern.stitches:
        x = scale*x
        y = -scale*y
        if command == JUMP:
            turtle.color("red")
            turtle.goto(x, y)

            speed = turtle.speed()
            turtle.speed('fastest')
            centered_dot(turtle, 5)
            turtle.speed(speed)
        elif command == TRIM:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            turtle.color("black")
            speed = turtle.speed()
            turtle.speed('fastest')
            centered_cross(turtle, 5)
            turtle.speed(speed)
        elif command == STITCH:
            turtle.setheading(turtle.towards(x, y))
            turtle.pendown()
            turtle.color("blue")
            turtle.goto(x, y)
            speed = turtle.speed()
            turtle.speed('fastest')
            centered_line(turtle, 3)
            turtle.speed(speed)
        else:
            raise ValueError(f"Command not supported: {command}")
