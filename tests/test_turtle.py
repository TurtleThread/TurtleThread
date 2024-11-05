import math
from math import copysign, cos, degrees, pi, radians, sin, sqrt

import pytest
from pyembroidery import JUMP, STITCH, TRIM
from pytest import approx

import turtlethread.stitches
from turtlethread import Turtle
from turtlethread.base_turtle import Vec2D


@pytest.fixture
def turtle():
    return Turtle(angle_mode="degrees")


def approx_list(nested_list):
    for element in nested_list:
        if type(element) == list:
            return [approx_list(el) for el in nested_list]
        else:
            return approx(nested_list)


class TestTurtle:
    @pytest.mark.parametrize("angle", [0, -10, 10])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    def test_angle_property_set(self, turtle, angle, angle_mode):
        turtle.angle_mode = angle_mode
        turtle.angle = angle
        assert turtle.angle == pytest.approx(angle % turtle._fullcircle)

    @pytest.mark.parametrize("angle", [0, -10, 10])
    def test_angle_property_correct_switch_degrees_radians(self, turtle, angle):
        turtle.angle_mode = "degrees"
        turtle.angle = angle
        turtle.angle_mode = "radians"
        assert turtle.angle == radians(angle % 360)

    @pytest.mark.parametrize("angle", [0, -pi / 4, pi])
    def test_angle_property_correct_switch_radians_degrees(self, turtle, angle):
        turtle.angle_mode = "radians"
        turtle.angle = angle
        turtle.angle_mode = "degrees"
        assert turtle.angle == degrees(angle) % 360

    @pytest.mark.parametrize("angle", [0, -10, 10])
    def test_heading_same_as_angle(self, turtle, angle):
        turtle.setheading(angle)
        assert turtle.heading() == turtle.angle
        assert turtle.angle == angle % 360

    @pytest.mark.parametrize("invalid_input", [0, 0.0, [0], float("nan"), float("inf")])
    def test_angle_mode_fails_for_invalid_input_type(self, turtle, invalid_input):
        with pytest.raises(TypeError):
            turtle.angle_mode = invalid_input

    def test_angle_mode_fails_for_invalid_input_value(self, turtle):
        with pytest.raises(KeyError):
            turtle.angle_mode = "invalid_string_input"

    def test_turtle_left(self, turtle):
        turtle.left(90)
        assert turtle.angle == 90

    def test_turtle_right(self, turtle):
        turtle.right(90)
        assert turtle.angle == 270

    @pytest.mark.parametrize("invalid_radius", [float("inf"), float("-inf"), float("-nan")])
    def test_circle_fails_for_invalid_radius(self, turtle, invalid_radius):
        with pytest.raises(ValueError):
            turtle.circle(invalid_radius)

    def test_circle_warns_for_zero_radius(self, turtle):
        with pytest.warns(UserWarning):
            turtle.circle(0)

    def test_home_resets_angle(self, turtle):
        turtle.angle = 3
        turtle.home()
        assert turtle.angle == 0

    def test_home_resets_position(self, turtle):
        turtle.goto(20, 20)
        turtle.home()
        assert turtle.x == 0
        assert turtle.y == 0

    @pytest.mark.parametrize("x", [0, -10, 10])
    @pytest.mark.parametrize("y", [0, -10, 10])
    def test_goto_changes_position(self, turtle, x, y):
        turtle.goto(x, y)
        assert turtle.x == x
        assert turtle.y == y

    @pytest.mark.parametrize("steps", [1, 2, 5, 10])
    @pytest.mark.parametrize("radius", [0, 1, 5, 10])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    def test_circle_stops_and_starts_in_same_position(self, turtle, radius, steps, angle_mode):
        turtle.angle_mode = angle_mode
        start_x = turtle.x
        start_y = turtle.y

        turtle.circle(radius=radius, steps=steps)

        assert turtle.x == approx(start_x)
        assert turtle.y == approx(start_y)

    @pytest.mark.parametrize("steps", [1, 2, 5, 10])
    @pytest.mark.parametrize("radius", [-1, 0, 1, 5, 10])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    def test_circle_stops_and_starts_with_same_angle(self, turtle, radius, steps, angle_mode):
        turtle.angle_mode = angle_mode
        start_angle = math.radians(turtle.angle * turtle._degreesPerAU)

        turtle.circle(radius=radius, steps=steps)

        end_angle = math.radians(turtle.angle * turtle._degreesPerAU)
        assert end_angle == approx(start_angle)

    def test_circle_considers_radius_sign(self, turtle):
        turtle.angle_mode = "radians"
        turtle.angle = 0
        turtle.circle(radius=100, extent=pi, steps=1)
        assert turtle.x == pytest.approx(0)
        assert turtle.y == pytest.approx(200)
        turtle.home()
        turtle.circle(radius=-100, extent=pi, steps=1)
        assert turtle.x == pytest.approx(0)
        assert turtle.y == pytest.approx(-200)

    def test_use_stitch_group_fails_if_inconsistent_state(self, turtle):
        with pytest.raises(RuntimeError):
            with turtle.running_stitch(20):
                with turtle.running_stitch(20):
                    turtle.cleanup_stitch_type()

    @pytest.mark.parametrize(
        "stitch_group",
        [
            turtlethread.stitches.JumpStitch(Vec2D(0, 0)),
            turtlethread.stitches.RunningStitch(Vec2D(0, 0), 20),
            turtlethread.stitches.TripleStitch(Vec2D(0, 0), 20),
        ],
    )
    def test_set_stitch_type_sets_stitch_type(self, turtle, stitch_group):
        turtle.set_stitch_type(stitch_group)
        assert turtle._stitch_group_stack[-1] is stitch_group

    def test_nested_stitch_context(self, turtle):
        with turtle.running_stitch(20):
            turtle.forward(20)
            with turtle.running_stitch(10):
                turtle.forward(20)
            turtle.forward(20)

            with turtle.running_stitch(10):
                turtle.forward(20)
                with turtle.running_stitch(5):
                    turtle.forward(10)
            turtle.forward(20)

            with turtle.jump_stitch():
                turtle.forward(50)
                with turtle.running_stitch(10):
                    turtle.forward(20)
                turtle.forward(20)
            turtle.forward(20)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert stitches == [
            (0, 0, STITCH),  # Parent running stitch group
            (20, 0, STITCH),
            (20, 0, STITCH),  # First nested running stitch group
            (30, 0, STITCH),
            (40, 0, STITCH),
            (40, 0, STITCH),  # Back to parent running  stitch group
            (60, 0, STITCH),
            (60, 0, STITCH),  # Second nested running  stitch group
            (70, 0, STITCH),
            (80, 0, STITCH),
            (80, 0, STITCH),  # Doubly nested running  stitch group
            (85, 0, STITCH),
            (90, 0, STITCH),
            (90, 0, STITCH),  # Back to parent running stitch group
            (110, 0, STITCH),
            (110, 0, TRIM),  # Nested jump stitch
            (160, 0, JUMP),
            (160, 0, STITCH),  # Running stich within nested jump stitch
            (170, 0, STITCH),
            (180, 0, STITCH),
            (180, 0, TRIM),  # Back to jump stitch
            (200, 0, JUMP),
            (200, 0, STITCH),  # Back to parent running stitch
            (220, 0, STITCH),
        ]


class TestTurtleJumpStitch:
    def test_turtle_jump_stitch_context(self, turtle):
        # Check that we get a trim command in the beginning
        # TODO: Maybe more?
        with turtle.jump_stitch():
            assert isinstance(turtle._stitch_group_stack[-1], turtlethread.stitches.JumpStitch)
        assert not turtle.pattern.to_pyembroidery().stitches

    def test_turtle_forward(self, turtle):
        """Test ``turtle.forward`` with different angles."""
        with turtle.jump_stitch(skip_intermediate_jumps=False):
            turtle.angle = 0
            turtle.forward(10)

            turtle.angle = 90
            turtle.forward(10)

            turtle.angle = 45
            turtle.forward(10)

            turtle.angle = 45 + 180
            turtle.forward(10)

        assert turtle.pattern.to_pyembroidery().stitches == approx_list(
            [
                [0, 0, TRIM],  # From the jump_stitch context manager. Should this be here?
                [10.0, 0, JUMP],
                [10.0, 10.0, JUMP],
                [10 * (1 + sin(pi / 4)), 10 * (1 + sin(pi / 4)), JUMP],
                [10.0, 10.0, JUMP],
            ]
        )

    def test_turtle_backward(self, turtle):
        """Test ``turtle.backward`` with different angles."""
        with turtle.jump_stitch(skip_intermediate_jumps=False):
            turtle.angle = 0
            turtle.backward(10)

            turtle.angle = 90
            turtle.backward(10)

            turtle.angle = 45
            turtle.backward(10)

            turtle.angle = 45 + 180
            turtle.backward(10)

        assert turtle.pattern.to_pyembroidery().stitches == approx_list(
            [
                [0, 0, TRIM],  # From the jump_stitch context manager.
                [-10.0, 0, JUMP],
                [-10.0, -10.0, JUMP],
                [-10 * (1 + sin(pi / 4)), -10 * (1 + sin(pi / 4)), JUMP],
                [-10.0, -10.0, JUMP],
            ]
        )

    @pytest.mark.parametrize("steps", [1, 2, 5, 10])
    @pytest.mark.parametrize("extent", [30, 90, 180, 360])
    @pytest.mark.parametrize("radius", [0, 1, 5, 10])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    @pytest.mark.parametrize("skip_intermediate_jumps", [True, False])
    def test_circle(self, turtle, radius, extent, steps, angle_mode, skip_intermediate_jumps):
        turtle.angle_mode = angle_mode
        with turtle.jump_stitch(skip_intermediate_jumps=skip_intermediate_jumps):
            turtle.angle = 0
            turtle.circle(radius, extent=extent, steps=steps)

        center_x = 0
        center_y = radius
        if skip_intermediate_jumps:
            # Only two stitches (TRIM and JUMP)
            assert len(turtle.pattern.to_pyembroidery().stitches) == 2
        else:
            # One JUMP stitch for every step and an additional TRIM stitch
            assert len(turtle.pattern.to_pyembroidery().stitches) == steps + 1

        for x, y, stitch_type in turtle.pattern.to_pyembroidery().stitches[1:]:
            distance_to_center = sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            assert distance_to_center == approx(radius)
            assert stitch_type == JUMP

    @pytest.mark.parametrize("x", [0, -10, 10])
    @pytest.mark.parametrize("y", [0, -10, 10])
    def test_goto(self, turtle, x, y):
        with turtle.jump_stitch():
            turtle.goto(x, y)

        assert turtle.pattern.to_pyembroidery().stitches == approx_list(
            [
                [0, 0, TRIM],  # From the jump_stitch context manager.
                [x, y, JUMP],
            ]
        )

    @pytest.mark.parametrize("x", [0, -10, 10])
    @pytest.mark.parametrize("y", [0, -10, 10])
    def test_home(self, turtle, x, y):
        with turtle.jump_stitch(skip_intermediate_jumps=False):
            turtle.goto(x, y)
            turtle.home()

        assert turtle.pattern.to_pyembroidery().stitches == approx_list(
            [
                [0, 0, TRIM],  # From the jump_stitch context manager.
                [x, y, JUMP],
                [0, 0, JUMP],
            ]
        )

    def test_start_jump_stitch_sets_stitch_type(self, turtle):
        turtle.start_jump_stitch()
        assert isinstance(turtle._stitch_group_stack[-1], turtlethread.stitches.JumpStitch)


class TestTurtleRunningStitch:
    @pytest.mark.parametrize("radius", [0, 1, 10])
    @pytest.mark.parametrize("extent", [30, 90, 180, 360])
    @pytest.mark.parametrize("steps", [1, 2, 4, 10])
    @pytest.mark.parametrize("stitch_length", [1, 10, 20])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    def test_circle(self, turtle, stitch_length, radius, extent, steps, angle_mode):
        """
        Test that all stitches are inside the circle given by `radius`
        and outside the incircle of the polygon with `steps` sides and
        radius equal `radius`.

        This test only works for extent <= full revolution. Otherwise, we may not create
        a regular polygon with the computed inner radius.
        """
        turtle.angle_mode = angle_mode
        if angle_mode == "radians":
            extent = radians(extent)
        inner_radius = radius * cos(pi / steps)

        with turtle.running_stitch(stitch_length):
            turtle.circle(radius, extent=extent, steps=steps)

        center_x = 0
        center_y = radius
        tol = 10e-8
        for x, y, stitch_type in turtle.pattern.to_pyembroidery().stitches[1:]:
            distance_to_center = sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            assert distance_to_center <= radius + tol
            assert distance_to_center >= inner_radius - tol
            assert stitch_type == STITCH

    @pytest.mark.parametrize("radius", [0, 2, 10, 100])
    @pytest.mark.parametrize("extent", [30, 90, 180, 360])
    @pytest.mark.parametrize("steps", [1, 2, 4, 10])
    @pytest.mark.parametrize("stitch_length", [1, 10, 20, 1000])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    def test_circle_subsequent_step_length(self, turtle, stitch_length, radius, extent, steps, angle_mode):
        """
        Test that any subsquent stitches has distance between 0.5*stitch_length and 1.5*stitch_length
        """
        turtle.angle_mode = angle_mode
        with turtle.running_stitch(stitch_length):
            turtle.circle(radius, extent=extent, steps=steps)

        extent = math.radians(extent * turtle._degreesPerAU)
        side_length = 2 * radius * sin(0.5 * extent / steps)
        tol = 1e-8
        pyemb_pattern = turtle.pattern.to_pyembroidery()
        for (x1, y1, st1), (x2, y2, st2) in zip(pyemb_pattern.stitches[1:], pyemb_pattern.stitches[2:]):
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            assert distance >= min(0.5 * stitch_length, side_length) - tol
            assert distance < 1.5 * stitch_length + tol

    @pytest.mark.parametrize("radius", [50, 100, 200])
    @pytest.mark.parametrize("extent", [30, 90, 180, 360])
    @pytest.mark.parametrize("stitch_length", [1, 5, 10, 20, 30])
    @pytest.mark.parametrize("angle_mode", ["degrees", "radians"])
    def test_circle_subsequent_step_length_when_step_not_given(self, turtle, stitch_length, radius, extent, angle_mode):
        turtle.angle_mode = angle_mode
        with turtle.running_stitch(stitch_length):
            turtle.circle(radius, extent=extent, steps=None)
        n_steps = turtle._steps_from_stitch_length(stitch_length, radius, extent)

        pyemb_pattern = turtle.pattern.to_pyembroidery()
        assert len(pyemb_pattern.stitches) == n_steps + 1
        for (x1, y1, st1), (x2, y2, st2) in zip(pyemb_pattern.stitches[1:], pyemb_pattern.stitches[2:]):
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            assert distance >= 0.5 * stitch_length
            assert distance < 1.5 * stitch_length

    @pytest.mark.parametrize("radius", [30, 50, 100])
    @pytest.mark.parametrize("extent", [30, 90, 180, 360])
    @pytest.mark.parametrize("stitch_length", [1, 2, 10])
    def test_n_sides_from_side_length(self, turtle, stitch_length, radius, extent):
        steps = turtle._n_sides_from_side_length(stitch_length, radius, radians(extent))
        step_length = 2 * radius * sin(radians(0.5 * extent) / steps)
        assert step_length == approx(stitch_length)

    def test_too_long_stitches_for_steps_calculation(self, turtle):
        with pytest.warns(UserWarning):
            with turtle.running_stitch(100):
                turtle.circle(10, steps=None)
        assert len(turtle.pattern.to_pyembroidery().stitches) == 5

    def test_just_one_step_for_zero_radius(self, turtle):
        with pytest.warns(UserWarning):
            with turtle.running_stitch(5):
                turtle.circle(0, steps=None)
        assert len(turtle.pattern.to_pyembroidery().stitches) == 2

    @pytest.mark.parametrize("stitch_length", [1, 2, 10, 30])
    @pytest.mark.parametrize("step_length", [10, 100, 500])
    def test_forward_different_stitch_lengths(self, turtle, stitch_length, step_length):
        with turtle.running_stitch(stitch_length):
            turtle.forward(step_length)

        stitches = turtle.pattern.to_pyembroidery().stitches
        for (x1, y1, st1), (x2, y2, st2) in zip(stitches[1:-2], stitches[2:-1]):
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            assert st1 == st2 == STITCH
            assert distance == approx(stitch_length)

        x1, y1, st1 = stitches[-2]
        x2, y2, st2 = stitches[-1]
        assert st1 == st2 == STITCH
        final_distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if step_length >= 0.5 * stitch_length:
            assert final_distance >= 0.5 * stitch_length
            assert final_distance < 1.5 * stitch_length
        else:
            assert final_distance == approx(step_length)

    @pytest.mark.parametrize("stitch_length", [1, 2, 10, 30])
    @pytest.mark.parametrize("step_length", [10, 100, 500])
    def test_backward_different_stitch_lengths(self, turtle, stitch_length, step_length):
        with turtle.running_stitch(stitch_length):
            turtle.backward(step_length)

        stitches = turtle.pattern.to_pyembroidery().stitches
        for (x1, y1, st1), (x2, y2, st2) in zip(stitches[1:-2], stitches[2:-1]):
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            assert st1 == st2 == STITCH
            assert distance == approx(stitch_length)

        x1, y1, st1 = stitches[-2]
        x2, y2, st2 = stitches[-1]
        assert st1 == st2 == STITCH
        final_distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if step_length >= 0.5 * stitch_length:
            assert final_distance >= 0.5 * stitch_length
            assert final_distance < 1.5 * stitch_length
        else:
            assert final_distance == approx(step_length)

    def test_start_running_stitch_sets_stitch_type(self, turtle):
        turtle.start_running_stitch(10)
        assert isinstance(turtle._stitch_group_stack[-1], turtlethread.stitches.RunningStitch)


class TestTurtleTripleStitch:
    @pytest.mark.parametrize("stitch_length", [2, 5, 10, 20, 50, 100])
    @pytest.mark.parametrize("step_scaling_factor", [0.1, 0.5, 1])
    def test_forward_single_step(self, turtle, stitch_length, step_scaling_factor):
        with turtle.triple_stitch(stitch_length):
            turtle.forward(stitch_length * step_scaling_factor)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert len(stitches) == 4
        assert stitches[0] == (0, 0, STITCH)
        assert stitches[1] == (stitch_length * step_scaling_factor, 0, STITCH)
        assert stitches[2] == stitches[0]
        assert stitches[3] == stitches[1]

    @pytest.mark.parametrize("stitch_length", [2, 5, 10, 20, 50, 100])
    def test_forward_two_steps(self, turtle, stitch_length):
        with turtle.triple_stitch(stitch_length):
            turtle.forward(2 * stitch_length)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert len(stitches) == 7
        assert stitches[0] == (0, 0, STITCH)
        assert stitches[1] == (stitch_length, 0, STITCH)
        assert stitches[2] == stitches[0]
        assert stitches[3] == stitches[1]
        assert stitches[4] == (stitch_length * 2, 0, STITCH)
        assert stitches[5] == stitches[3]
        assert stitches[6] == stitches[4]

    @pytest.mark.parametrize("stitch_length", [2, 5, 10, 20, 50, 100])
    def test_forward_single_step_twice(self, turtle, stitch_length):
        with turtle.triple_stitch(stitch_length):
            turtle.forward(stitch_length)
            turtle.forward(stitch_length)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert len(stitches) == 7
        assert stitches[0] == (0, 0, STITCH)
        assert stitches[1] == (stitch_length, 0, STITCH)
        assert stitches[2] == stitches[0]
        assert stitches[3] == stitches[1]
        assert stitches[4] == (stitch_length * 2, 0, STITCH)
        assert stitches[5] == stitches[3]
        assert stitches[6] == stitches[4]

    @pytest.mark.parametrize("stitch_length", [2, 5, 10, 20, 50, 100])
    @pytest.mark.parametrize("steps", [4, 5, 10])
    def test_circle(self, turtle, stitch_length, steps):
        """We get the correct number of stitches when creating a circle.

        Here, we use a circle with at least 4 steps, i.e. a square. To make sure that each side consists of only one
        stitch, we set the radius to stitch_length, which will give us maximum side lengths of sqrt(2)*stitch_length
        (for 4 steps). Since this is less than 1.5*stitch_length, we only get a single stitch per side of the square.
        """
        with turtle.triple_stitch(stitch_length):
            turtle.circle(stitch_length, steps=steps)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert len(stitches) == 3 * steps + 1

    def test_start_triple_stitch_sets_stitch_type(self, turtle):
        turtle.start_triple_stitch(10)
        assert isinstance(turtle._stitch_group_stack[-1], turtlethread.stitches.TripleStitch)


class TestTurtleZigzagStitch:
    # TODO: Add more test cases, preferably concrete ones
    @pytest.mark.parametrize("density", [1, 5, 20, 50])
    @pytest.mark.parametrize("width", [1, 5, 20, 50])
    @pytest.mark.parametrize("center", [True, False])
    def test_zigzag_stitch(self, turtle, density, width, center):
        with turtle.zigzag_stitch(density, width, center=center):
            turtle.forward(100)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert len(stitches) > 0

class TestTurtleSatinStitch:
    # TODO: Add more test cases
    @pytest.mark.parametrize("width", [1, 5, 20, 50])
    @pytest.mark.parametrize("center", [True, False])
    def test_zigzag_stitch(self, turtle, width, center):
        with turtle.satin_stitch(width, center=center):
            turtle.forward(100)

        stitches = turtle.pattern.to_pyembroidery().stitches
        assert len(stitches) > 0