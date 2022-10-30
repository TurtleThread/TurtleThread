import math
from contextlib import contextmanager
from enum import Enum, auto
from warnings import warn

from pyembroidery import JUMP, STITCH, TRIM, EmbPattern, write

from .pattern_info import show_info
from .visualise import visualise_pattern

USE_SPHINX_GALLERY = False


class ConfigValue(Enum):
    @classmethod
    def get(cls, item):
        valid_items = {enum.name.lower() for enum in cls}
        if item.lower() not in valid_items:
            raise KeyError(f"{item} is not a valid {cls.__name__}. Must be one of {valid_items} (case insensitive)")
        return cls[item.upper()]


class AngleMode(ConfigValue):
    RADIANS = auto()
    DEGREES = auto()


class Turtle:
    """Turtle object that to make embroidery files. Mirrored after the official `turtle <https://docs.python.org/3/library/turtle.html>`_ library.

    Any undocumented functions have the same interface as the official turtle library.

    One turtle-step is equivalent to 0.1 mm.

    Parameters
    ----------
    pattern : pyembroidery.EmbPattern (optional)
        The embroidery pattern to work with. If not supplied, then an empty pattern will be created.
    angle_mode : "degrees" or "radians" (optional, default="degrees")
        How angles are computed.
    scale : float (optional, default=1)
        Scaling between turtle steps and units in the embroidery file. Below are some example scaling

         * `scale=1`  - One step is one unit in the embroidery file (0.1 mm)
         * `scale=10` - One step equals 1 mm
         * `scale=2`  - The scaling TurtleStitch uses
    """

    def __init__(self, pattern=None, angle_mode="degrees", scale=1):
        # TODO: Flag that can enable/disable changing angle when angle mode is changed
        if pattern is None:
            self.pattern = EmbPattern()
        else:
            self.pattern = pattern

        # TODO: What should be default?
        self.stitch_type = "no_stitch"
        self.stitch_parameters = {"length": 10}
        self._previous_stitch_type = [self.stitch_type]
        self._previous_stitch_parameters = [self.stitch_parameters]
        self.angle_mode = angle_mode
        self.scale = scale

        self.angle = 0
        self.x = 0
        self.y = 0

        # For integration with sphinx-gallery
        self._gallery_patterns = []

    @property
    def angle_mode(self):
        """The angle mode, either "degrees" or "radians"."""
        return self._angle_mode

    @angle_mode.setter
    def angle_mode(self, value):
        """Setter that ensures that a valid angle mode is used."""
        if isinstance(value, AngleMode):
            self._angle_mode = value
        elif isinstance(value, str):
            self._angle_mode = AngleMode.get(value.upper())
        else:
            raise TypeError(f"Angle mode must be a string or {AngleMode}")

    @property
    def angle(self):
        if self.angle_mode == AngleMode.RADIANS:
            return self._angle
        elif self.angle_mode == AngleMode.DEGREES:
            return math.degrees(self._angle)

    @angle.setter
    def angle(self, value):
        self._angle = self._to_counter_clockwise_radians(value)

    def _steps_from_stitch_length(self, stitch_length, radius, extent):
        if radius == 0:
            steps = 1
        elif 0.5 * stitch_length / radius > math.sin(math.pi / 4):
            steps = 4
            warn(
                "Cannot calculate `steps` based on `stitch_length` as `stitch_length` is too long compared"
                + " to `radius`. A minimum no. `steps` of 4 is chosen instead. To disable this either provide"
                + " `steps`, decrease `stitch_length` or increase the circle `radius`"
            )
        else:
            extent = self._to_counter_clockwise_radians(extent)
            steps = self._n_sides_from_side_length(stitch_length, radius, extent)
            steps = int(round(steps))
        return steps

    def _n_sides_from_side_length(self, side_length, radius, extent):
        # Assumes that radius is converted to radians prior to call
        return extent / (2 * math.asin(0.5 * side_length / radius))

    def circle(self, radius, extent=None, steps=None):
        """Draw a circle, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.circle>`_."""
        if radius == 0:  # TODO: Maybe use a lower tolerance
            warn("Drawing a circle with radius is 0 is not possible and may lead to many stitches in the same spot")
        if math.isinf(radius) or math.isnan(radius):
            raise ValueError(f"``radius`` cannot be nan or inf, it is {radius}")

        if self.angle_mode == AngleMode.DEGREES:
            fullcircle = 360
        else:
            fullcircle = 2 * math.pi

        if extent is None:
            extent = fullcircle

        if steps is None and "length" in self.stitch_parameters:
            stitch_length = self.stitch_parameters["length"]
            steps = self._steps_from_stitch_length(stitch_length, abs(radius), extent)
        elif steps is None:
            steps = 20

        w = math.copysign(extent, radius) / steps
        angle = 0.5 * w
        sidelength = 2 * radius * math.sin(self._to_counter_clockwise_radians(angle))

        self.left(0.5 * w)
        for i in range(steps):
            self.forward(sidelength)
            self.left(w)
        self.right(0.5 * w)

    def position(self):
        """Get the position, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.position>`_."""
        return self.x, self.y

    def _push_settings(self):
        self._previous_stitch_type.append(self.stitch_type)
        self._previous_stitch_parameters.append(self.stitch_parameters)

    def _pop_settings(self):
        self.stitch_type = self._previous_stitch_type.pop()
        self.stitch_parameters = self._previous_stitch_parameters.pop()

    def start_running_stitch(self, stitch_length):
        """Set the stitch mode to running stitch (not recommended, use ``running_stitch``-context instead).

        With a running stitch, we get stitches with a constant distance between each stitch.

        One step is equivalent to 0.1 mm, we recommend setting the minimum length
        between each stitch to 30 (3 mm).

        It is recommended to use the ``running_stitch``-context instead of the start-functions
        since they will automatically cleanup afterwards.

        Parameters
        ----------
        stitch_length : int
            Number of steps between each stitch.
        """
        # Store current settings
        self._push_settings()

        # Set stitch parameters
        self.stitch_type = "running_stitch"
        self.stitch_parameters = {"length": stitch_length}

        # Initialise stitch
        self.pattern.add_stitch_absolute(STITCH, self.x, self.y)

    def start_jump_stitch(self):
        """Set the stitch mode to jump-stitch (not recommended, use ``jump_stitch``-context instead).

        With a jump-stitch, trim the thread and move the needle without sewing more stitches.
        """
        # Store current settings
        self._push_settings()

        # Set stitch parameters
        self.stitch_type = "jump_stitch"
        self.stitch_parameters = {}
        self.pattern.add_stitch_absolute(TRIM, self.x, self.y)

    def cleanup_stitch_type(self):
        """Cleanup after switching to running stitch."""
        self._pop_settings()

    @contextmanager
    def running_stitch(self, stitch_length):
        """Set the stitch mode to running stitch and cleanup afterwards.

        With a running stitch, we get stitches with a constant distance between each stitch.

        One step is equivalent to 0.1 mm, we recommend setting the minimum length
        between each stitch to 30 (3 mm).

        Parameters
        ----------
        stitch_length : int
            Number of steps between each stitch.
        """
        self.start_running_stitch(stitch_length)
        yield
        self._pop_settings()

    @contextmanager
    def jump_stitch(self):
        """Set the stitch mode to jump-stitch and cleanup afterwards.

        With a jump-stitch, trim the thread and move the needle without sewing more stitches.
        """
        # Store current settings
        self.start_jump_stitch()

        yield

        # Reset settings
        self.stitch_type = self._previous_stitch_type.pop()
        self.stitch_parameters = self._previous_stitch_parameters.pop()
        # TODO: Possibly a flag for cleaning up the stitches-list so we only have a single jump command after the trim

    def _goto_running_stitch(self, x, y):
        x, y = self.scale * x, self.scale * y
        distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        angle = math.atan2(y - self.y, x - self.x)
        step_length = self.stitch_parameters["length"]

        # TODO: Maybe add a flag in the stitch parameters to customise this behaviour.

        # Running to the exact stopping point. The final stitch will be between 0.5 and 1.5 times the
        # stitch length.

        # First, the needle does stitches until the distance to the end-point is
        # less than two stitch-lengths away
        distance_traveled = 0
        while distance_traveled + 2 * step_length < distance:
            self.x += step_length * math.cos(angle)
            self.y += step_length * math.sin(angle)
            self.pattern.add_stitch_absolute(STITCH, self.x, self.y)
            distance_traveled += step_length

        # Then, we check if we need one final stitch, to prevent stitches larger than
        # 1.5 times the stitch length
        if distance - distance_traveled >= 1.5 * step_length:
            self.x += step_length * math.cos(angle)
            self.y += step_length * math.sin(angle)
            self.pattern.add_stitch_absolute(STITCH, self.x, self.y)
            distance_traveled += step_length

        # We add the final stitch at the end-point, which is guaranteed to be at most 1.5 and at least 0.5
        # stitch-lengths away from the second to last stitch.
        self.x = x
        self.y = y
        self.pattern.add_stitch_absolute(STITCH, self.x, self.y)

    def _goto_jump_stitch(self, x, y):
        self.x = self.scale * x
        self.y = self.scale * y
        self.pattern.add_stitch_absolute(JUMP, self.x, self.y)

    def _goto_no_stitch(self, x, y):
        self.x = self.scale * x
        self.y = self.scale * y

    def goto(self, x, y):
        """Goto a given position, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.goto>`_."""
        if self.stitch_type == "running_stitch":
            self._goto_running_stitch(x, y)
        elif self.stitch_type == "jump_stitch":
            self._goto_jump_stitch(x, y)
        elif self.stitch_type == "no_stitch":
            self._goto_no_stitch(x, y)
        else:
            raise ValueError(f"{self.stitch_type} is not a valid stitch pattern")

    def forward(self, distance):
        """Move forward a set distance, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.forward>`_."""
        x = self.x + distance * math.cos(self._angle)
        y = self.y + distance * math.sin(self._angle)
        self.goto(x, y)

    def backward(self, distance):
        """Move backward a set distance, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.backward>`_."""
        self.forward(-distance)

    def _rotate(self, angle):
        self.angle += angle

    def right(self, angle):
        """Rotate right the specified angle, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.right>`_."""
        self._rotate(angle)

    def left(self, angle):
        """Rotate left the specified angle, see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.left>`_."""
        self._rotate(-angle)

    def save(self, filename):
        """Save the embroidery pattern as an embroidery or image file.

        Saves the embroiery pattern to file. Supports standard embroidery file formats,
        such as ``.dst``, ``.jef`` and ``.pes``, and utility formats such as ``.png``,
        ``.svg`` and ``.txt``. For a full list of supported file formats, see the `pyembroidery documentation <https://github.com/EmbroidePy/pyembroidery#file-io>`_.

        Parameters
        ----------
        filename : str
        """
        if not USE_SPHINX_GALLERY:
            write(self.pattern, filename)
        else:
            self._gallery_patterns.append((filename, self.pattern.copy()))

    def setheading(self, angle):
        """Set the turtle's heading, 0 degrees is pointing right. See the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.setheading>`_."""
        self.angle = angle

    def home(self):
        """Move the needle home (position (0, 0)), see the `official documentation <https://docs.python.org/3/library/turtle.html#turtle.home>`_."""
        self.goto(0, 0)
        self.angle = 0

    def visualise(self, turtle=None, width=800, height=800, scale=1, done=True, bye=True):
        """Use the builtin ``turtle`` library to visualise this turtle's embroidery pattern.

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
        visualise_pattern(self.pattern, turtle=turtle, width=width, height=height, scale=scale, done=done, bye=bye)

    def show_info(self):
        """Display information about this turtle's embroidery pattern."""
        show_info(self.pattern, scale=self.scale)

    def heading(self):
        """Returns the turtle's heading (i.e. angle)

        writing ``turtle.heading()`` gives the same result as writing ``turtle.angle``.
        """
        return self.angle

    def _to_counter_clockwise_radians(self, angle):
        if self.angle_mode == AngleMode.DEGREES:
            return math.radians(angle)
        elif self.angle_mode == AngleMode.RADIANS:
            return angle

    fd = forward
    bk = backward
    back = backward
    rt = right
    lt = left
    setpos = goto
    setposition = goto
    seth = setheading
    pos = position
