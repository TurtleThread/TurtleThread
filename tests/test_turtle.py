from turtlethread import Turtle
import pytest
from math import degrees, pi, sin, sqrt, cos, radians
from pyembroidery import JUMP, TRIM, STITCH
from pytest import approx


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
    @pytest.mark.parametrize('angle', [0, -10, 10])
    def test_to_counter_clockwise_radians(self, turtle, angle):
        turtle.angle_mode = "degrees"
        assert turtle._to_counter_clockwise_radians(angle) == radians(angle)
        turtle.angle_mode = "radians"
        assert turtle._to_counter_clockwise_radians(angle) == angle

    @pytest.mark.parametrize('angle', [0, -10, 10])
    @pytest.mark.parametrize('angle_mode', ["degrees", "radians"])
    def test_angle_property_set(self, turtle, angle, angle_mode):
        turtle.angle_mode = angle_mode
        turtle.angle = angle
        assert turtle.angle == angle

    @pytest.mark.parametrize('angle', [0, -10, 10])
    def test_angle_property_correct_switch_degrees_radians(self, turtle, angle):
        turtle.angle_mode = "degrees"
        turtle.angle = angle
        turtle.angle_mode = "radians"
        assert turtle.angle == radians(angle)

    @pytest.mark.parametrize('angle', [0, -pi/4, pi])
    def test_angle_property_correct_switch_radians_degrees(self, turtle, angle):
        turtle.angle_mode = "radians"
        turtle.angle = angle
        turtle.angle_mode = "degrees"
        assert turtle.angle == degrees(angle)

    @pytest.mark.parametrize('angle', [0, -10, 10])
    def test_heading_same_as_angle(self, turtle, angle):
        turtle.setheading(angle)
        assert turtle.heading() == turtle.angle
        assert turtle.angle == angle

    @pytest.mark.parametrize('invalid_input', [0, 0.0, [0], float("nan"), float("inf")])
    def test_angle_mode_fails_for_invalid_input_type(self, turtle, invalid_input):
        with pytest.raises(TypeError):
            turtle.angle_mode = invalid_input

    def test_angle_mode_fails_for_invalid_input_value(self, turtle):
        with pytest.raises(ValueError):
            turtle.angle_mode = "invalid_string_input"


    def test_turtle_left(self, turtle):
        turtle.left(90)
        assert turtle.angle == -90  # y-axis points down to be consistent with turtlestitch

    def test_turtle_right(self, turtle):
        turtle.right(90)
        assert turtle.angle == 90  # y-axis points down to be consistent with turtlestitch

    @pytest.mark.parametrize('invalid_radius', [float("inf"), float("-inf"), float("-nan")])
    def test_circle_fails_for_invalid_radius(self, turtle, invalid_radius):
        with pytest.raises(ValueError):
            turtle.circle(invalid_radius)

    def test_circle_warns_for_zero_radius(self, turtle):
        with pytest.warns(UserWarning):
            turtle.circle(0)


class TestTurtleJumpStitch:
    def test_turtle_jump_stitch_context(self, turtle):
        # Check that we get a trim command in the beginning
        # Maybe more?
        with turtle.jump_stitch():
            assert turtle.stitch_type == "jump_stitch"
        assert turtle.pattern.stitches == [[0, 0, TRIM]]

    def test_turtle_forward(self, turtle):
        """Test ``turtle.forward`` with different angles.
        """
        with turtle.jump_stitch():
            turtle.angle = 0
            turtle.forward(10)
            
            turtle.angle = 90
            turtle.forward(10)
            
            turtle.angle = 45
            turtle.forward(10)

            turtle.angle = 45+180
            turtle.forward(10)

        assert turtle.pattern.stitches == approx_list([
            [0, 0, TRIM],  # From the jump_stitch context manager. Should this be here?
            [10., 0, JUMP],
            [10., 10., JUMP],
            [10*(1 + sin(pi/4)), 10*(1 + sin(pi/4)), JUMP],
            [10., 10., JUMP],
        ])

    def test_turtle_backward(self, turtle):
        """Test ``turtle.backward`` with different angles.
        """
        with turtle.jump_stitch():
            turtle.angle = 0
            turtle.backward(10)
            
            turtle.angle = 90
            turtle.backward(10)
            
            turtle.angle = 45
            turtle.backward(10)

            turtle.angle = 45+180
            turtle.backward(10)
        
        assert turtle.pattern.stitches == approx_list([
            [0, 0, TRIM],  # From the jump_stitch context manager. 
            [-10., 0, JUMP],
            [-10., -10., JUMP],
            [-10*(1 + sin(pi/4)), -10*(1 + sin(pi/4)), JUMP],
            [-10., -10., JUMP],
        ])

    @pytest.mark.parametrize('steps', [1, 2, 5, 10])
    @pytest.mark.parametrize('extent', [30, 90, 180, 360])
    @pytest.mark.parametrize('radius', [0, 1, 5, 10])
    def test_circle(self, turtle, radius, extent, steps):
        with turtle.jump_stitch():
            turtle.angle = 0
            turtle.circle(radius, extent=extent, steps=steps)

        center_x = 0
        center_y = -radius
        assert len(turtle.pattern.stitches) == steps + 1
        for (x, y, stitch_type) in turtle.pattern.stitches[1:]:
            distance_to_center = sqrt((x - center_x)**2 + (y - center_y)**2)
            assert distance_to_center == approx(radius)
            assert stitch_type == JUMP


    @pytest.mark.parametrize('x', [0, -10, 10])
    @pytest.mark.parametrize('y', [0, -10, 10])
    def test_goto(self, turtle, x, y):
        with turtle.jump_stitch():
            turtle.goto(x, y)

        assert turtle.pattern.stitches == approx_list([
            [0, 0, TRIM],  # From the jump_stitch context manager. 
            [x, y, JUMP],
        ])

    @pytest.mark.parametrize('x', [0, -10, 10])
    @pytest.mark.parametrize('y', [0, -10, 10])
    def test_home(self, turtle, x, y):
        with turtle.jump_stitch():
            turtle.goto(x, y)
            turtle.home()
        
        assert turtle.pattern.stitches == approx_list([
            [0, 0, TRIM],  # From the jump_stitch context manager. 
            [x, y, JUMP],
            [0, 0, JUMP],
        ])


class TestTurtleRunningStitch:
    @pytest.mark.parametrize('radius', [0, 1, 10])
    @pytest.mark.parametrize('extent', [30, 90, 180, 360])
    @pytest.mark.parametrize('steps', [1, 2, 4, 10])
    @pytest.mark.parametrize('stitch_length', [1, 10, 20])
    def test_circle(self, turtle, stitch_length, radius, extent, steps):
        """
        Test that all stitches are inside the circle given by `radius`
        and outside the incircle of the polygon with `steps` sides and
        radius equal `radius`
        """
        inner_radius = radius * cos(pi/steps)

        with turtle.running_stitch(stitch_length):
            turtle.circle(radius, extent=extent, steps=steps)

        center_x = 0
        center_y = -radius
        tol = 10e-8
        for (x, y, stitch_type) in turtle.pattern.stitches[1:]:
            distance_to_center = sqrt((x - center_x)**2 + (y - center_y)**2)
            assert distance_to_center <= radius + tol
            assert distance_to_center >= inner_radius - tol
            assert stitch_type == STITCH

    @pytest.mark.parametrize('radius', [0, 2, 10, 100])
    @pytest.mark.parametrize('extent', [30, 90, 180, 360])
    @pytest.mark.parametrize('steps', [1, 2, 4, 10])
    @pytest.mark.parametrize('stitch_length', [1, 10, 20, 1000])
    @pytest.mark.parametrize('angle_mode', ['degrees', 'radians'])
    def test_circle_subsequent_step_length(self, turtle, stitch_length, radius, extent, steps, angle_mode):
        """
        Test that any subsquent stitches has distance between 0.5*stitch_length and 1.5*stitch_length
        """
        turtle.angle_mode = angle_mode
        with turtle.running_stitch(stitch_length):
            turtle.circle(radius, extent=extent, steps=steps)

        extent = turtle._to_counter_clockwise_radians(extent)
        side_length = 2*radius*sin(0.5*extent/steps)
        tol = 1e-8
        for (x1, y1, st1), (x2, y2, st2) in zip(turtle.pattern.stitches[1:], turtle.pattern.stitches[2:]):
            distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            assert distance >= min(0.5*stitch_length, side_length) - tol
            assert distance < 1.5*stitch_length + tol

    @pytest.mark.parametrize('radius', [50, 100, 200])
    @pytest.mark.parametrize('extent', [30, 90, 180, 360])
    @pytest.mark.parametrize('stitch_length', [1, 5, 10, 20, 30])
    def test_circle_subsequent_step_length_when_step_not_given(self, turtle, stitch_length, radius, extent):        
        with turtle.running_stitch(stitch_length):
            turtle.circle(radius, extent=extent, steps=None)
        n_steps = turtle._steps_from_stitch_length(stitch_length, radius, extent)
        
        assert len(turtle.pattern.stitches) == n_steps + 1
        for (x1, y1, st1), (x2, y2, st2) in zip(turtle.pattern.stitches[1:], turtle.pattern.stitches[2:]):
            distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            assert distance >= 0.5*stitch_length
            assert distance < 1.5*stitch_length

    @pytest.mark.parametrize('radius', [30, 50, 100])
    @pytest.mark.parametrize('extent', [30, 90, 180, 360])
    @pytest.mark.parametrize('stitch_length', [1, 2, 10])
    def test_n_sides_from_side_length(self, turtle, stitch_length, radius, extent):
        steps = turtle._n_sides_from_side_length(stitch_length, radius, radians(extent))
        step_length = 2*radius*sin(radians(0.5*extent)/steps)
        assert step_length == approx(stitch_length)

    def test_too_long_stitches_for_steps_calculation(self, turtle):
        with pytest.warns(UserWarning):
            with turtle.running_stitch(100):
                turtle.circle(10, steps=None)
        assert len(turtle.pattern.stitches) == 5

    def test_just_one_step_for_zero_radius(self, turtle):
        with pytest.warns(UserWarning):
            with turtle.running_stitch(5):
                turtle.circle(0, steps=None)
        assert len(turtle.pattern.stitches) == 2
