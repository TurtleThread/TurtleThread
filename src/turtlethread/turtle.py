import math
from contextlib import contextmanager
from enum import Enum
from warnings import warn

from pyembroidery import write

from . import stitches
from .base_turtle import TNavigator, Vec2D
from .pattern_info import show_info
from .visualise import visualise_pattern

USE_SPHINX_GALLERY = False


class ConfigValueMixin:
    NO_VALUE = object()

    @classmethod
    def get(cls, item, default=NO_VALUE):
        if isinstance(item, cls):
            return item
        valid_items = {enum.name.lower() for enum in cls}
        if item.lower() not in valid_items and default is cls.NO_VALUE:
            raise KeyError(f"{item} is not a valid {cls.__name__}. Must be one of {valid_items} (case insensitive)")
        elif item.lower() not in valid_items:
            return default

        return cls[item.upper()]


class AngleMode(ConfigValueMixin, Enum):
    RADIANS = "radians"
    DEGREES = "degrees"


class Turtle(TNavigator):
    """Turtle object that to make embroidery files. Mirrored after the official :py:mod:`turtle` library.

    This class has the same API as the builtin ``turtle.Turtle`` class with documented changes, for more information
    see the official documentation of the
    `builtin turtle library <https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions>`_

    One turtle-step is equivalent to 0.1 mm (unless scaled otherwise).

    Parameters
    ----------
    pattern : turtlethread.stitches.EmbroideryPattern (optional)
        The embroidery pattern to work with. If not supplied, then an empty pattern will be created.
    scale : float (optional, default=1)
        Scaling between turtle steps and units in the embroidery file. Below are some example scaling

         * `scale=1`  - One step is one unit in the embroidery file (0.1 mm)
         * `scale=10` - One step equals 1 mm
         * `scale=2`  - The scaling TurtleStitch uses
    angle_mode : "degrees" or "radians" (optional, default="degrees")
        How angles are computed.
    mode : "standard", "world" or "logo" (optional, default="standard")
        Mode "standard" is compatible with turtle.py.
        Mode "logo" is compatible with most Logo-Turtle-Graphics.
        Mode "world" is the same as 'standard' for TurtleThread.

        .. list-table::
            :header-rows: 1

            * - Mode
              - Initial turtle heading
              - Positive angles
            * - ``"standard"``
              - To the right (east)
              - Counterclockwise
            * - ``"logo"``
              - Upward (north)
              - Clockwise

    """

    def __init__(self, pattern=None, scale=1, angle_mode="degrees", mode=TNavigator.DEFAULT_MODE):
        # TODO: Flag that can enable/disable changing angle when angle mode is changed
        if pattern is None:
            self.pattern = stitches.EmbroideryPattern(scale=scale)
        else:
            self.pattern = pattern

        # Set up stitch parameters prior to super.__init__ since self.reset() depends on stitch type
        self._stitch_group_stack = []

        super().__init__(mode=mode)
        self.angle_mode = angle_mode

        # For integration with sphinx-gallery
        self._gallery_patterns = []

    @property
    def angle_mode(self):
        """The angle mode, either "degrees" or "radians"."""
        if abs(self._degreesPerAU - 1) < 1e-5:
            return "degrees"
        elif abs(self._degreesPerAU - 360 / math.tau) < 1e-5:
            return "radians"
        else:
            return "other (_setDegreesPerAU has been called explicitly)"

    @angle_mode.setter
    def angle_mode(self, value):
        """Setter that ensures that a valid angle mode is used."""
        if not isinstance(value, (str, AngleMode)):
            raise TypeError(f"Angle mode must be one of 'degrees' or 'radians' (case insensitive), not {value}")

        if AngleMode.get(value, None) == AngleMode.DEGREES:
            self.degrees()
        elif AngleMode.get(value, None) == AngleMode.RADIANS:
            self.radians()
        else:
            raise KeyError(f"Angle mode must be one of 'degrees' or 'radians' (case insensitive), not {value}")

    @property
    def angle(self):
        return self.heading()

    @angle.setter
    def angle(self, value):
        self.setheading(value)

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
            extent = math.radians(extent * self._degreesPerAU)
            steps = self._n_sides_from_side_length(stitch_length, radius, extent)
            steps = int(round(steps))
        return steps

    def _n_sides_from_side_length(self, side_length, radius, extent):
        # Assumes that radius is converted to radians prior to call
        return extent / (2 * math.asin(0.5 * side_length / radius))

    def circle(self, radius, extent=None, steps=None):
        """Draw a circle or arc, for more info see the official :py:func:`turtle.circle` documentation.

        Parameters
        ----------
        radius: float
            Radius of the circle
        extent: float
            The angle of the arc, by default it is a full circle
        steps: float
            The circle is approximated as a sequence of ``steps`` line segments. If the ``steps`` are not given, then the optimal number
            of line segments for the current stitch length is selected.
        """
        if radius == 0:  # TODO: Maybe use a lower tolerance
            warn("Drawing a circle with radius is 0 is not possible and may lead to many stitches in the same spot")
        if math.isinf(radius) or math.isnan(radius):
            raise ValueError(f"``radius`` cannot be nan or inf, it is {radius}")

        if extent is None:
            extent = self._fullcircle

        if (
            steps is None
            and self._stitch_group_stack  # The stitch group stack is not empty
            and hasattr(self._stitch_group_stack[-1], "stitch_length")  # length is specified in topmost stitch group
        ):
            stitch_length = self._stitch_group_stack[-1].stitch_length
            steps = self._steps_from_stitch_length(stitch_length, abs(radius), extent)
        elif steps is None:
            steps = 20

        super().circle(radius=radius, extent=extent, steps=steps)

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
        self.set_stitch_type(stitches.RunningStitch(self.pos(), stitch_length))

    def start_triple_stitch(self, stitch_length):
        """Set the stitch mode to triple stitch (not recommended, use ``triple_stitch``-context instead).

        Triple stitch is equivalent to running stitch, but the thread moves back and forth three times for each stitch.

        One step is equivalent to 0.1 mm, we recommend setting the minimum length between each stitch to 30 (3 mm).

        Parameters
        ----------
        stitch_length : int
            Number of steps between each stitch.
        """
        self.set_stitch_type(stitches.TripleStitch(self.pos(), stitch_length))

    def start_jump_stitch(self):
        """Set the stitch mode to jump-stitch (not recommended, use ``jump_stitch``-context instead).

        With a jump-stitch, trim the thread and move the needle without sewing more stitches.
        """
        self.set_stitch_type(stitches.JumpStitch(self.pos()))

    def cleanup_stitch_type(self):
        """Cleanup after switching stitch type."""
        self._stitch_group_stack.pop()
        if self._stitch_group_stack:
            # This handles nested context managers. We remove the top stitch group
            # from the stack and make a copy of it that we place back. We do it this
            # way so the starting position of the copy is where the the turtle is right
            # now.
            previous_stitch_group = self._stitch_group_stack.pop()
            stitch_group = previous_stitch_group.empty_copy(self.position())

            self._stitch_group_stack.append(stitch_group)
            self.pattern.stitch_groups.append(stitch_group)

    def set_stitch_type(self, stitch_group):
        self._stitch_group_stack.append(stitch_group)
        self.pattern.stitch_groups.append(stitch_group)

    @contextmanager
    def use_stitch_group(self, stitch_group):
        self.set_stitch_type(stitch_group=stitch_group)
        yield
        if self._stitch_group_stack[-1]._parent_stitch_group is not stitch_group:
            raise RuntimeError(
                "Inconsistent state, likely caused by explicitly calling `cleanup_stitch_type` within a"
                + " stitch group context (e.g. within a `with turtle.running_stitch(20):` block)."
                + "\nYou should either set stitch groups with context managers or with the `start_{stitch_type}`"
                + " methods, not both."
            )
        self.cleanup_stitch_type()

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
        return self.use_stitch_group(stitches.RunningStitch(self.pos(), stitch_length))

    def triple_stitch(self, stitch_length):
        """Set the stitch mode to triple stitch and cleanup afterwards.

        Triple stitch is equivalent to running stitch, but the thread moves back and forth three times for each stitch.

        One step is equivalent to 0.1 mm, we recommend setting the minimum length between each stitch to 30 (3 mm).

        Parameters
        ----------
        stitch_length : int
            Number of steps between each stitch.
        """
        return self.use_stitch_group(stitches.TripleStitch(self.pos(), stitch_length))

    def jump_stitch(self, skip_intermediate_jumps=True):
        """Set the stitch mode to jump-stitch and cleanup afterwards.

        With a jump-stitch, trim the thread and move the needle without sewing more stitches.

        Parameters
        ----------
        skip_intermediate_jumps : bool (optional, default=True)
            If True, then multiple jump commands will be collapsed into one jump command. This is useful in the cases
            where there may be multiple subsequent jumps with no stitches inbetween. Multiple subsequent jumps doesn't
            make sense but it can happen dependent on how you generate your patterns.
        """
        return self.use_stitch_group(stitches.JumpStitch(self.pos(), skip_intermediate_jumps=skip_intermediate_jumps))

    @property
    def _position(self):
        return Vec2D(self.x, self.y)

    @_position.setter
    def _position(self, other):
        """Goto a given position, see the :py:meth:`goto` documentation for more info."""
        if self._stitch_group_stack:
            self._stitch_group_stack[-1].add_location(other)
        self.x, self.y = other

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
            write(self.pattern.to_pyembroidery(), filename)
        else:
            self._gallery_patterns.append((filename, self.pattern.to_pyembroidery()))

    def home(self):
        """Move the needle home (position (0, 0)), for more info see the official :py:func:`turtle.home` documentation"""
        self.goto(0, 0)
        self.angle = 0

    def visualise(self, turtle=None, width=800, height=800, scale=1, trace_jump=False, done=True, bye=True):
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
        trace_jump : bool
            If True, then draw a grey line connecting the origin and destination of jumps.
        done : bool
            If True, then ``turtle.done()`` will be called after drawing.
        bye : bool
            If True, then ``turtle.bye()`` will be called after drawing.
        """
        visualise_pattern(
            self.pattern.to_pyembroidery(),
            turtle=turtle, width=width, height=height, scale=scale, trace_jump=trace_jump, done=done, bye=bye
        )

    def show_info(self):
        """Display information about this turtle's embroidery pattern."""
        show_info(self.pattern.to_pyembroidery(), scale=self.pattern.scale)
