import argparse
import turtle
from pathlib import Path

import turtlethread
import turtlethread.visualise as visualise


def bye():
    for i in range(2):
        try:
            turtle.bye()
        except turtle.Terminator:
            pass


def draw_stamp(func, filename):
    turt = turtle.Turtle()
    screen = turtle.Screen()
    for length in range(3):
        func(turt, length * 5)
        turt.forward(50)

    func(turt, length * 5 + 5)

    screen.getcanvas().postscript(file=filename)
    bye()


def draw_square_flower(filename):
    pen = turtlethread.Turtle()
    screen = turtle.Screen()
    num_petals = 8

    with pen.running_stitch(30):
        for petal in range(num_petals):
            for side in range(4):
                pen.forward(300)
                pen.right(90)
            pen.right(360 / num_petals)

    pen.visualise(done=False, bye=False)
    screen.getcanvas().postscript(file=filename)
    bye()


def draw_test_scene(filename):
    turt = turtlethread.Turtle()
    screen = turtle.Screen()
    with turt.running_stitch(40):
        turt.circle(30)
        turt.circle(50)
        turt.circle(100)
        turt.forward(100)
        turt.right(90)
        turt.backward(50)
        turt.left(45)
        turt.forward(20)

    with turt.jump_stitch(skip_intermediate_jumps=False):
        turt.circle(30)
        turt.circle(50)
        turt.circle(100)
        turt.forward(100)
        turt.right(90)
        turt.backward(50)
        turt.left(45)
        turt.forward(20)

    turt.visualise(done=False, bye=False)
    screen.getcanvas().postscript(file=filename)
    bye()


def draw_empty_scene(filename):
    pen = turtlethread.Turtle()
    screen = turtle.Screen()
    pen.visualise(done=False, bye=False)
    screen.getcanvas().postscript(file=filename)
    bye()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out_dir",
        help="Output directory. If not given, then __file__/visualise_postscript will be used.",
        type=str,
        default=None,
    )

    args = parser.parse_args()
    if args.out_dir is None:
        out_dir = Path(__file__).parent / "visualise_postscript"
    else:
        out_dir = Path(args.out_dir)

    out_dir.mkdir(parents=True, exist_ok=True)
    draw_stamp(visualise.centered_dot, out_dir / "centered_dot.eps")
    draw_stamp(visualise.centered_cross, out_dir / "centered_cross.eps")
    draw_stamp(visualise.centered_line, out_dir / "centered_line.eps")
    draw_square_flower(out_dir / "square_flower.eps")
    draw_test_scene(out_dir / "test_scene.eps")
    draw_empty_scene(out_dir / "empty_scene.eps")
