import math
import random
from contextlib import contextmanager

from pyembroidery import JUMP, STITCH, EmbPattern, write


# TODO: Method to visualise with Turtle
class Turtle:
    def __init__(self, pattern=None, angle_mode="degrees"):
        if pattern is None:
            self.pattern = EmbPattern()
        else:
            self.pattern = pattern
        self.angle = 0
        self.x = 0
        self.y = 0

        # TODO: What should be default?
        self.stitch_type = "no_stitch"
        self.stitch_parameters = {"length": 10}
        self._previous_stitch_type = self.stitch_type
        self._previous_stitch_parameters = self.stitch_parameters
        self.angle_mode = angle_mode

    @property
    def angle_mode(self):
        return self._angle_mode
    
    @angle_mode.setter
    def angle_mode(self, value):
        if not isinstance(value, str):
            raise TypeError("Angle mode must be a string")
        elif value.lower() not in {"degrees", "radians"}:
            raise ValueError(f"Angle mode must be either degrees or radians, not {angle_mode}")
        else:
            self._angle_mode = value.lower()

    def _cos(self, angle):
        if self.angle_mode == "degrees":
            angle = math.radians(angle)
        return math.cos(angle)

    def _sin(self, angle):
        if self.angle_mode == "degrees":
            angle = math.radians(angle)
        return math.sin(angle)

    def circle(self, radius, extent=None, steps=None):
        if self.angle_mode == "degrees":
            fullcircle = 360
        else:
            fullcircle = 2*math.pi

        if extent is None:
            extent = fullcircle

        if steps is None:
            # TODO: implement so that number of steps can be based on length of running stitch
            steps = 20

        w = 1.0 * extent / steps

        angle = math.radians(0.5 * w)
        sidelength = 2 * radius * math.sin(angle)

        self.left(0.5 * w)
        for i in range(steps):
            self.forward(sidelength)
            self.left(w)
        self.right(0.5 * w)

    def position(self):
        return self.x, self.y

    @contextmanager
    def running_stitch(self, stitch_length):
        # Store current settings
        self._previous_stitch_type = self.stitch_type
        self._previous_stitch_parameters = self.stitch_parameters

        # Set stitch parameters
        self.stitch_type = "running_stitch"
        self.stitch_parameters = {"length": stitch_length}

        # Initialise stitch
        self.pattern.add_stitch_absolute(STITCH, self.x, self.y)
        yield

        # Reset settings
        self.stitch_type = self._previous_stitch_type
        self.stitch_parameters = self._previous_stitch_parameters

    @contextmanager
    def jump_stitch(self):
        # Store current settings
        self._previous_stitch_type = self.stitch_type
        self._previous_stitch_parameters = self.stitch_parameters

        # Set stitch parameters
        self.stitch_type = "jump_stitch"
        self.stitch_parameters = {}

        yield

        # Reset settings
        self.stitch_type = self._previous_stitch_type
        self.stitch_parameters = self._previous_stitch_parameters

    def _goto_running_stitch(self, x, y):
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
        self.x = x
        self.y = y
        self.pattern.add_stitch_absolute(JUMP, self.x, self.y)

    def _goto_no_stitch(self, x, y):
        self.x = x
        self.y = y

    def goto(self, x, y):
        if self.stitch_type == "running_stitch":
            self._goto_running_stitch(x, y)
        elif self.stitch_type == "jump_stitch":
            self._goto_jump_stitch(x, y)
        elif self.stitch_type == "no_stitch":
            self._goto_no_stitch(x, y)
        else:
            raise ValueError(f"{self.stitch_type} is not a valid stitch pattern")

    def forward(self, distance):
        x = self.x + distance * self._cos(self.angle)
        y = self.y + distance * self._sin(self.angle)
        self.goto(x, y)

    def backward(self, distance):
        self.forward(-distance)

    def _rotate(self, angle):
        self.angle += angle

    def right(self, angle):
        self._rotate(angle)

    def left(self, angle):
        self._rotate(-angle)

    def save(self, filename):
        """Save the embroidery pattern as an embroidery or image file.

        Saves the embroiery pattern to file. Supports standard embroidery file formats,
        such as ``.dst``, ``.jef`` and ``.pes``, and utility formats such as ``.png``,
        ``.svg`` and ``.txt``. For a full list of supported file formats, see the `pyembroidery documentation <https://github.com/EmbroidePy/pyembroidery#file-io>`.

        Arguments
        ---------
        filename : str
        """
        write(self.pattern, filename)

    def setheading(self, angle):
        self.angle = angle

    def home(self):
        self.goto(0, 0)
        self.angle = 0

    fd = forward
    bk = backward
    back = backward
    rt = right
    lt = left
    setpos = goto
    setposition = goto
    seth = setheading
    pos = position
