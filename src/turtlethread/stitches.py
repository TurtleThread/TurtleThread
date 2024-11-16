from __future__ import annotations

import itertools
import math
from abc import ABC, abstractmethod
from copy import copy
from typing import Any, Generator, Iterable
import warnings

try:
    from typing import Literal, Self, TypeAlias
except ImportError:
    from typing_extensions import Literal, Self, TypeAlias

import pyembroidery

from .base_turtle import Vec2D

# STITCH=0, JUMP=1, TRIM=2, ZIGZAG=3, SATIN=4, CROSS=5
StitchCommand: TypeAlias = Literal[0, 1, 2, 3, 4, 5]


class EmbroideryPattern:
    """Abstract representation of an embroidery pattern.

    Container object

    Parameters
    ----------
    scale: int (optional, default=1)
        All coordinates are multiplied by this parameter before converting it to a PyEmbroidery pattern.
        This is useful to control the number of steps per mm (default is 10 steps per mm).
    """

    def __init__(self, scale: int = 1) -> None:
        self.stitch_groups: list[StitchGroup | EmbroideryPattern] = []
        self.scale = scale

    def to_pyembroidery(self) -> pyembroidery.EmbPattern:
        """Convert to a PyEmbroidery pattern."""
        pattern = pyembroidery.EmbPattern()
        for stitch_group in self.stitch_groups:
            scaled_stitch_commands = (
                (x * self.scale, y * self.scale, cmd) for x, y, cmd in stitch_group.get_stitch_commands()
            )
            pattern.stitches.extend(scaled_stitch_commands)

        return pattern

    def get_stitch_command(self) -> list[tuple[float, float, StitchCommand]]:
        """Get stitch commands for PyEmbroidery.

        This function is used when embroidery patterns contain whole embroidery patterns. If you're not explicitly
        making patterns within patterns, then you probably want to use the :py:meth:`to_pyembroidery` method instead.
        """
        for stitch_group in self.stitch_groups:
            yield from stitch_group.get_stitch_commands()


class StitchGroup(ABC):
    """Object representing one contiguous set of commands for the embroidery machine.

    Stitch groups are used to convert the Turtle commands into embroidery machine commands. For example, if you want to
    embroider with a running stitch, then you'd create a stitch group for a running stitch with the corresponding
    stitch length.

    Stitch groups work by storing subsequent locations of the Turtle and converts them into embroidery commands.

    Parameters
    ----------
    start_pos: Vec2D (tuple[float, float])
        The initial position of the turtle.
    """

    def __init__(self, start_pos: Vec2D) -> None:
        self._start_pos = start_pos
        self._positions = []
        self._stitch_commands = None
        self._parent_stitch_group = self

    def add_location(self, location: Vec2D) -> None:
        """Add a new location to this stitch group."""
        self._stitch_commands = None
        self._positions.append(location)

    @abstractmethod
    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        raise NotImplementedError

    def get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        """Get the list of PyEmbroidery stitch commands for this stitch group"""
        if self._stitch_commands is None:
            self._stitch_commands = self._get_stitch_commands()

        return self._stitch_commands.copy()

    def empty_copy(self, start_pos) -> Self:
        """Create a copy of the stitch group but with no stored locations (i.e. no stitches)."""
        copied_group = copy(self)
        copied_group._positions = []
        copied_group._start_pos = start_pos
        copied_group._parent_stitch_group = self._parent_stitch_group

        return copied_group


class UnitStitch(StitchGroup):
    """Class to represent stitches that are built off repeating a single pattern, e.g. zigzag, cross stitches.

    Given the distance to travel, the stitch will be repeated the required number of times to reach that distance.

    Contains a starting stitch and an ending stitch function. These functions will be called once at the start and
    end of the overall stitch, respectively. This is useful, for example, for centering stitches.

    Parameters
    ----------
    stitch_length : int
        Number of steps between each unit stitch, in the direction of travel. If auto-adjustment is not enabled, this
        will be the exact number of steps between each unit stitch.
    auto_adjust : bool (optional, default=True)
        If True, the stitch length will be automatically adjusted to a multiple of the distance travelled. Useful
        when only drawing a single forward or backwards stitch. 
        If False, the stitch length will be exactly ``stitch_length``. A final stitch will be added to the end position
        unless enforce_end_position is False.
    enforce_end_stitch : bool (optional, default=True)
        If True, the final stitch must be positioned at the end position. This will ensure that the total length of the
        stitch is the total distance to be traveled. 
        If False, there is no such guarantee. Any ending stitch will not occur.
        Useful in conjunction with enforce_start_stitch, to seamlessly blend two stitches together.
    enforce_start_stitch : bool (optional, default=True)
        If True, the first stitch must be positioned at the start position. 
        If False, the starting stitch pattern will not occur.

    Internal Attributes
    -------------------
    stitch_stop_multiplier : float (default=0)
        When stitching, the unit stitch will be repeated until there is stitch_stop_multiplier * stitch_length left to
        stitch. Useful when implementing an ending stitch pattern.
    """
    def __init__(
        self, 
        start_pos: Vec2D, 
        stitch_length: int | float, 
        auto_adjust: bool = True, 
        enforce_end_stitch: bool = True, 
        enforce_start_stitch: bool = True) -> None:

        super().__init__(start_pos=start_pos)
        self.stitch_length = stitch_length
        self.auto_adjust = auto_adjust
        self.enforce_end_stitch = enforce_end_stitch
        self.enforce_start_stitch = enforce_start_stitch

        self.stitch_stop_multiplier

    @classmethod
    def round_stitch_length(cls, stitch_length : int | float, distance : int | float):
        """Method to round the stitch length to a multiple of the distance.

        Parameters
        ----------
        stitch_length : int | float
            The stitch length to round.
        distance : int | float
            The distance of travel.
        """
        if distance < stitch_length: 
            # Stitch length cannot be less than the total distance
            return distance 

        # Find the closest stitch_length that is a multiple of stitch_length
        return stitch_length/round(stitch_length/density)
         
    def _start_stitch_unit(self, start_pos: Vec2D, angle: float, stitch_length: float) -> list[tuple[float, float, StitchCommand]]:
        """Stitch a pattern at the start of a stitch. To be implemented by children.
        The stitch should start from start_pos, but should not have a stitch at that position.
        There should be a stitch at the end position.

        Due to the many variations in the distance travelled in this section, children are encouraged to use the
        nonlocal keyword to access the variables x and y, which should be set to the end position after the starting
        stitch pattern, as well as the distance_traveled variable to set the distance travelled along the direction
        of the stitch.

        Parameters
        ----------
        start_pos: Vec2D (tuple[float, float])
            The start position of the stitch.
        angle: float    
            The angle of the stitch.
        stitch_length: float
            The stitch length of the stitch.
        """
        nonlocal x, y, distance_traveled
        pass
        
    def _stitch_unit(self, start_pos: Vec2D, angle: float, stitch_length: float) -> list[tuple[float, float, StitchCommand]]:
        """Stitch a single unit. To be implemented by children.
        The stitch should start from start_pos, but should not have a stitch at that position.
        There should be a stitch at the end position.

        Parameters
        ----------
        start_pos: Vec2D (tuple[float, float])
            The start position of the stitch.
        angle: float    
            The angle of the stitch.
        stitch_length: float
            The stitch length of the stitch.
        """
        raise NotImplementedError

    def _end_stitch_unit(self, start_pos: Vec2D, angle: float, stitch_length: float) -> list[tuple[float, float, StitchCommand]]:
        """Stitch a pattern at the start of a stitch. To be implemented by children.
        The stitch should start from start_pos, but should not have a stitch at that position.
        There should NOT be a stitch at the end position.

        Due to the many variations in the distance travelled in this section, children are encouraged to use the
        nonlocal keyword to access the variables x and y, which should be set to the end position after the starting
        stitch pattern, as well as the distance_traveled variable to set the distance travelled along the direction
        of the stitch.

        Parameters
        ----------
        start_pos: Vec2D (tuple[float, float])
            The start position of the stitch.
        angle: float    
            The angle of the stitch.
        stitch_length: float
            The stitch length of the stitch.
        """
        nonlocal x, y, distance_traveled
        pass
    
    def _iter_stitches_between_positions(
        self, position_1: Vec2D, position_2: Vec2D
    ) -> Generator[tuple[StitchCommand, float, float], None, None]:

        x, y = position_1
        x_end, y_end = position_2

        distance = math.sqrt((x - x_end) ** 2 + (y - y_end) ** 2)
        angle = math.atan2(y_end - y, x_end - x)
        dx = math.cos(angle)
        dy = math.sin(angle)

        distance_traveled = 0
        stitch_length = self.stitch_length
        if self.auto_adjust: # Adjust stitch length if auto-adjustment is enabled
            stitch_length = self.round_stitch_length(self.stitch_length, distance)

        if self.enforce_start_stitch:
            for stitch in self._start_stitch_unit(Vec2D(x, y), angle, stitch_length): yield stitch

        # Repeat until one stitch away
        while distance_traveled + stitch_length*self.stitch_stop_multiplier < distance:
            for stitch in self._stitch_unit(Vec2D(x, y), angle, stitch_length): yield stitch
            x += stitch_length * dx
            y += stitch_length * dy
            distance_traveled += stitch_length

        if self.enforce_end_stitch:
            for stitch in self._end_stitch_unit(Vec2D(x, y), angle, stitch_length): yield stitch
            yield x_end, y_end, pyembroidery.STITCH


    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        if not self._positions:
            return []

        stitch_commands = []

        # Start the stitch at the start position if enforce_start_stitch is True.
        if self.enforce_start_stitch:
            stitch_commands.append((self._start_pos[0], self._start_pos[1], pyembroidery.STITCH))

        stitch_commands.extend(self._iter_stitches_between_positions(self._start_pos, self._positions[0]))
        for pos1, pos2 in itertools.pairwise(self._positions):
            stitch_commands.extend(self._iter_stitches_between_positions(pos1, pos2))

        return stitch_commands


class RunningStitch(StitchGroup):
    """Stitch group for running stitches.

    With a running stitch, we get stitches with a constant distance between each stitch.

    If the turtle is supposed to move a number of steps that is not a multiple of ``stitch_length``, then all but the
    last stitch in that stretch will have the same length and the last stitch will be between ``0.5*stitch_length`` and
    ``1.5*stitch_length``.

    Parameters
    ----------
    stitch_length : int
        Number of steps between each stitch.
    """

    def __init__(self, start_pos: Vec2D, stitch_length: int | float) -> None:
        super().__init__(start_pos=start_pos)

        self.stitch_length = stitch_length

    def _iter_stitches_between_positions(
        self, position_1: Vec2D, position_2: Vec2D
    ) -> Generator[tuple[StitchCommand, float, float], None, None]:
        # Running stitch between two points, stopping exactly at position 2 and not
        # adding any stitch at position 1. The final stitch will be between 0.5 and 1.5
        # times the stitch length.
        x, y = position_1
        x_end, y_end = position_2

        distance = math.sqrt((x - x_end) ** 2 + (y - y_end) ** 2)
        angle = math.atan2(y_end - y, x_end - x)
        dx = math.cos(angle)
        dy = math.sin(angle)

        # First, the needle does stitches until the distance to the end-point is
        # less than two stitch-lengths away
        distance_traveled = 0
        while distance_traveled + 2 * self.stitch_length < distance:
            x += self.stitch_length * dx
            y += self.stitch_length * dy
            distance_traveled += self.stitch_length
            yield x, y, pyembroidery.STITCH

        # Then, we check if we need one final stitch, to prevent stitches larger than
        # 1.5 times the stitch length
        if distance - distance_traveled >= 1.5 * self.stitch_length:
            x += self.stitch_length * dx
            y += self.stitch_length * dy
            distance_traveled += self.stitch_length
            yield x, y, pyembroidery.STITCH

        # We add the final stitch at the end-point, which is guaranteed to be at most
        # 1.5 and at least 0.5 stitch-lengths away from the second to last stitch.
        yield x_end, y_end, pyembroidery.STITCH

    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        if not self._positions:
            return []

        stitch_commands = [(self._start_pos[0], self._start_pos[1], pyembroidery.STITCH)]
        stitch_commands.extend(self._iter_stitches_between_positions(self._start_pos, self._positions[0]))
        for pos1, pos2 in itertools.pairwise(self._positions):
            stitch_commands.extend(self._iter_stitches_between_positions(pos1, pos2))

        return stitch_commands


def iterate_back_and_forth(iterable: Iterable[Any]) -> Generator[tuple[StitchCommand, float, float], None, None]:
    """Iterates back and forth trough an iterable

    Each element (except the first) is given twice, with the previous element sandwiched inbetween.
    (So all element exept he first and last is given in total three times)

    Parameters
    ----------
    iterable
        Iterable to iterate back and forth over


    Yields
    ------
    Elements from the iterable

    >>> list(iterate_back_and_forth([0, 1, 2, 3]))
    [0, 1, 0, 1, 2, 1, 2, 3, 2, 3]
    """
    iterator = iter(iterable)
    previous = next(iterator)
    yield previous

    for item in iterator:
        yield item
        yield previous
        yield item
        previous = item


class TripleStitch(StitchGroup):
    """Stitch group for triple stitches.

    TripleStitch is the same as a :py:class:`RunningStitch`, but the thread moves back and forth three times for each
    stitch.

    Parameters
    ----------
    stitch_length : int
        Number of steps between each stitch.
    """

    def __init__(self, start_pos: Vec2D, stitch_length: float) -> None:
        super().__init__(start_pos=start_pos)
        self.running_stitch = RunningStitch(start_pos=start_pos, stitch_length=stitch_length)

    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        self.running_stitch._positions = self._positions
        stitch_commands = self.running_stitch._get_stitch_commands()

        return list(iterate_back_and_forth(stitch_commands))


class JumpStitch(StitchGroup):
    """Stitch group for jump stitches.

    A jump stitch group always starts with a trim command followed by the needle moving without sewing any stitches.

    See :py:class:`StitchGroup` for more information on stitch groups.

    Parameters
    ----------
    skip_intermediate_jumps : bool (optional, default=True)
        If True, then multiple jump commands will be collapsed into one jump command. This is useful in the cases
        where there may be multiple subsequent jumps with no stitches inbetween. Multiple subsequent jumps doesn't
        make sense but it can happen dependent on how you generate your patterns.
    """

    def __init__(self, start_pos: Vec2D, skip_intermediate_jumps: bool = True) -> None:
        super().__init__(start_pos=start_pos)
        self.skip_intermediate_jumps = skip_intermediate_jumps

    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        if not self._positions:
            return []

        stitch_commands = [(self._start_pos[0], self._start_pos[1], pyembroidery.TRIM)]
        if self.skip_intermediate_jumps:
            x, y = self._positions[-1]
            stitch_commands.append((x, y, pyembroidery.JUMP))
            return stitch_commands

        for x, y in self._positions:
            stitch_commands.append((x, y, pyembroidery.JUMP))
        return stitch_commands

class ZigzagStitch(StitchGroup):
    """Stitch group for zigzag stitches.

    With a zigzag stitch, we stitch in a zigzag pattern.

    By default, as the turtle moves forward, a stitch is done on the left then right side of the turtle, to get a
    zigzag. However, if center=False, the turtle will only form stitches on the right side of the path. 

    The 'density' of a zigzag is the distance between two stitches along the direction of the stitch. For example,
    if the turtle is moving horizontally, the density is the horizontal distance between two adjacent stitches on
    the zigzag.
    The 'width' is the number of steps between the left-most and right-most point of the zigzag stitch.

    When the turtle moves a distance that is not a multiple of the density, the program will adjust the density
    to the closest possible multiple. 

    Parameters
    ----------
    density : int
        Number of steps between two stitches along the direction of travel.
    width : int
        Number of steps between the left and right side of the zig-zag.
    center : boolean
        If True, then the turtle will form stitches on both the left and right side of the path. Else, the turtle 
        will only form stitches on the right side of the path.
    """

    def __init__(self, start_pos: Vec2D, density: int | float, width: int | float, center: bool = True) -> None:
        super().__init__(start_pos=start_pos)
        self.density = density 
        self.step_length = density
        self.width = width
        self.center = center

    @classmethod
    def round_density(cls, stitch_length : int | float, density : int | float, center : bool = True):
        if stitch_length < density: 
            return stitch_length # Density cannot be greater than stitch length
        if center or (not center and round(stitch_length/density) % 2 == 0):
            return stitch_length/round(stitch_length/density)
        else:
            # Odd number and not center
            return stitch_length/(round(stitch_length/density) + 1)
         
    def _iter_stitches_between_positions(
        self, position_1: Vec2D, position_2: Vec2D
    ) -> Generator[tuple[StitchCommand, float, float], None, None]:

        # Zigzag stitch between two points, stopping exactly at position 2 and not
        # adding any stitch at position 1. 
        x, y = position_1
        x_end, y_end = position_2

        distance = math.sqrt((x - x_end) ** 2 + (y - y_end) ** 2)
        angle = math.atan2(y_end - y, x_end - x)
        dx = math.cos(angle)
        dy = math.sin(angle)

        distance_traveled = 0
        stitch_length = self.round_density(distance, self.density, self.center)  
        if stitch_length < 2: warnings.warn("Stitch length is less than 0.2mm! This may cause your machine to jam.")
        should_go_right = True # Choose whether to go right or left next stitch

        if self.center:
            x += stitch_length/2 * dx
            y += stitch_length/2 * dy
            left_angle = angle + math.pi/2 # Left stitch is right angle to the direction of travel
            x = x + (self.width/2 * math.cos(left_angle)) # Going from center to left, hence half width
            y = y + (self.width/2 * math.sin(left_angle))
            yield x, y, pyembroidery.STITCH

        # Repeat until one stitch away
        while distance_traveled < distance - stitch_length:
            x += stitch_length * dx
            y += stitch_length * dy

            if should_go_right:
                right_angle = angle - math.pi/2 # Right stitch is also a right angle to the direction of travel
                stitch_x = x + (self.width * math.cos(right_angle)) # Going from left to right hence full width
                stitch_y = y + (self.width * math.sin(right_angle))
                yield stitch_x, stitch_y, pyembroidery.STITCH
            else:
                yield x, y, pyembroidery.STITCH # We are already at left position
            
            should_go_right = not should_go_right
            distance_traveled += stitch_length

        yield x_end, y_end, pyembroidery.STITCH

    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        if not self._positions:
            return []

        stitch_commands = [(self._start_pos[0], self._start_pos[1], pyembroidery.STITCH)]
        stitch_commands.extend(self._iter_stitches_between_positions(self._start_pos, self._positions[0]))
        for pos1, pos2 in itertools.pairwise(self._positions):
            stitch_commands.extend(self._iter_stitches_between_positions(pos1, pos2))

        return stitch_commands

class SatinStitch(ZigzagStitch):
    """Stitch group for satin stitches.

    A satin stitch is simply a zigzag stitch with a tight density. This creates a solid fill.
    We use 0.3mm for the density.

    The 'width' is the number of steps between the left-most and right-most point of the satin stitch.

    Parameters
    ----------
    width : int
        Number of steps between the left and right side of the stitch.
    center : boolean
        If True, then the turtle will form stitches on both the left and right side of the path. Else, the turtle 
        will only form stitches on the right side of the path.
    """

    def __init__(self, start_pos: Vec2D, width: int | float, center: bool = True) -> None:
        super().__init__(start_pos=start_pos, width=width, center=center, density=3)

class CrossStitch(StitchGroup):
    """Stitch group for cross stitches.

    A cross stitch is a stitch that stitches in a cross shape. Due to limitations with a sewing machine, it is
    not a true cross stich, as there is a visible line at the bottom connecting the 'crosses' in the stitch.

    This is also known as a Knit Overlock stitch.
    
    The cross stitch is implemented by going from the top left corner to the bottom right corner, then moving
    from the bottom right to the bottom left, before finally going to the top right corner. This corner will
    be the top left of the next cross stitch.

    If centered, start by moving by width/2 to the left, such that the center of the cross stitch is aligned
    with the original position of the turtle.

    The 'density' of the cross stitch is the distance between the left and right sides of the crosses. This 
    follows a similar formula to zigzag stitch.
    The 'width' of the cross stitch is the distance between the top and bottom of the cross stitch.

    Parameters
    ----------
    density : int | float
        Distance between the left and right sides of the cross stitch.
    width : int | float
        Distance between the top and bottom of the cross stitch.
    center : boolean
        If True, then the turtle will form stitches on both the left and right side of the path. Else, the turtle 
        will only form stitches on the right side of the path.
    """

    def __init__(self, start_pos: Vec2D, density: int | float, width: int | float, center: bool = True) -> None:
        super().__init__(start_pos=start_pos)
        self.density = density
        self.width = width
        self.center = center

    @classmethod
    def calculate_actual_density(cls, stitch_length : int | float, density : int | float):
        """Use a similar formula to zigzag stitch to find the actual density"""
        if stitch_length < density: 
            return stitch_length # Density cannot be greater than stitch length
        return max(1, stitch_length/round(stitch_length/density))

    def _iter_stitches_between_positions(
        self, position_1: Vec2D, position_2: Vec2D
    ) -> Generator[tuple[StitchCommand, float, float], None, None]:

        # Cross stitch between two points, stopping exactly at position 2 and not
        # adding any stitch at position 1. 
        x, y = position_1
        x_end, y_end = position_2

        stitch_length = math.sqrt((x - x_end) ** 2 + (y - y_end) ** 2)
        angle = math.atan2(y_end - y, x_end - x)
        dx = math.cos(angle)
        dy = math.sin(angle)

        # Calculate the actual density of the stitch
        density = CrossStitch.calculate_actual_density(stitch_length, self.density)

        if self.center:
            left_angle = angle + math.pi/2 # Turn left 90 degrees
            x += self.width/2 * math.cos(left_angle)
            y += self.width/2 * math.sin(left_angle)   
            yield x, y, pyembroidery.STITCH

        # Move to the end location of the stitch
        for _ in range(round(stitch_length/density)): # Round to prevent FP errors
            
            # TOP LEFT TO BOTTOM RIGHT

            # Top-Left to Top-Right
            x += self.density * dx 
            y += self.density * dy
            # Top-Right to Bottom-Right
            right_angle = angle - math.pi/2 # Turn right 90 degrees
            x += self.width * math.cos(right_angle)
            y += self.width * math.sin(right_angle)
            yield x, y, pyembroidery.STITCH

            # BOTTOM RIGHT TO BOTTOM LEFT 
            reverse_angle = angle + math.pi # Turn 180 degrees
            x -= self.density * dx 
            y -= self.density * dy
            yield x, y, pyembroidery.STITCH

            # BOTTOM LEFT TO TOP RIGHT
            
            # Bottom-Left to Top-Left
            left_angle = angle + math.pi/2 # Turn left 90 degrees 
            x += self.width * math.cos(left_angle)
            y += self.width * math.sin(left_angle)
            # Top-Left to Top-Right
            x += self.density * dx 
            y += self.density * dy
            yield x, y, pyembroidery.STITCH

        if self.center:
            right_angle = angle - math.pi/2 # Turn right 90 degrees
            x += self.width/2 * math.cos(right_angle)
            y += self.width/2 * math.sin(right_angle)   
            yield x, y, pyembroidery.STITCH


    def _get_stitch_commands(self) -> list[tuple[float, float, StitchCommand]]:
        if not self._positions:
            return []

        stitch_commands = [(self._start_pos[0], self._start_pos[1], pyembroidery.STITCH)]
        stitch_commands.extend(self._iter_stitches_between_positions(self._start_pos, self._positions[0]))
        for pos1, pos2 in itertools.pairwise(self._positions):
            stitch_commands.extend(self._iter_stitches_between_positions(pos1, pos2))

        return stitch_commands


