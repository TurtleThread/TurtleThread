from pathlib import Path
from tempfile import TemporaryDirectory

from pytest import fixture
import pytest

import turtlethread.visualise
from turtlethread.visualise import centered_dot, centered_line, centered_cross, visualise_pattern

from .create_postscript import draw_square_flower, draw_stamp, draw_test_scene

@fixture
def tempdir():
    tmpdir = TemporaryDirectory()
    try:
        yield Path(tmpdir.__enter__())
    finally:
        tmpdir.__exit__(None, None, None)


@fixture
def postscript_dir():
    return Path(__file__).parent / "visualise_postscript"


def iter_eps(eps):
    for line in eps.splitlines():
        out = line.split("%")[0]
        if out != "":
            yield out


def assert_eps_equal(eps_path, supposed_eps_path):
    with open(eps_path) as f:
        eps = f.read()

    with open(supposed_eps_path) as f:
        supposed_eps = f.read()

    for eps_line, supposed_line in zip(iter_eps(eps), iter_eps(supposed_eps)):
        if eps_line[0] != "%":
            assert eps_line == supposed_line, eps


@pytest.mark.tkinter
@pytest.mark.parametrize("stamp", ["centered_dot", "centered_cross", "centered_line"])
def test_stamp(tmpdir, postscript_dir, stamp):
    out = tmpdir / f"{stamp}.eps"
    supposed = postscript_dir / f"{stamp}.eps"

    draw_stamp(getattr(turtlethread.visualise, stamp), out)
    assert_eps_equal(out, supposed)


@pytest.mark.tkinter
def test_visualise_square_flower(tmpdir, postscript_dir):
    out = tmpdir / "square_flower.eps"
    supposed = postscript_dir / "square_flower.eps"

    draw_square_flower(out)
    assert_eps_equal(out, supposed)


@pytest.mark.tkinter
def test_visualise_test_scene(tmpdir, postscript_dir):
    out = tmpdir / "test_scene.eps"
    supposed = postscript_dir / "test_scene.eps"

    draw_test_scene(out)
    assert_eps_equal(out, supposed)
