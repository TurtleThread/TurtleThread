import math
from abc import ABC, abstractmethod
from .base_turtle import Vec2D


def rotate_point(x, y, angle):
    """Rotate a point around the origin by a given angle (in radians)."""
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x_new = x * cos_theta - y * sin_theta
    y_new = x * sin_theta + y * cos_theta
    return x_new, y_new

class Fill(ABC):
    """A class to represent a fill. This is a base class for other fill types.
    Given a list of points that make up a polygon, the fill() function should fill it in using the appropriate methods."""

    @abstractmethod
    def fill(self, points):
        raise NotImplementedError

class ScanlineFill(Fill):
    """The Scanline fill will create straight lines across the fill area to fill it up. Useful for small areas.

    Parameters
    -----------
    angle:
        Angle of the lines, in radians. May also be the string 'auto'.
        If 'auto', the program will automatically try the angles of 0, 45, 90, and 135 degrees, to minimize the number of jump stitches."""
    def __init__(self, angle : str | int | float):
        if type(angle) == str and angle == "auto":
            self.auto = True
        else:
            self.auto = False
            self.angle = angle
            
    def _fill_at_angle(self, turtle, points, angle, simulate=False):
        # Rotate the coordinates
        rot_points = []
        for x, y in points:
            x_rot, y_rot = rotate_point(x, y, angle)
            rot_points.append((x_rot, y_rot))

        # Basic scanline fill implementation
        edges = []
        min_x = rot_points[0][0]
        max_x = rot_points[0][0]
        min_y = rot_points[0][1]
        max_y = rot_points[0][1]
        for i in range(len(rot_points) - 1):
            edges.append((rot_points[i], rot_points[i + 1]))
            min_x = min(min_x, rot_points[i + 1][0])
            max_x = max(max_x, rot_points[i + 1][0])
            min_y = min(min_y, rot_points[i + 1][1])
            max_y = max(max_y, rot_points[i + 1][1])

        scanned_lines = []
        scanline_y = min_y
        while scanline_y <= max_y:
            intersections = []
            for edge in edges:
                if edge[0][1] <= scanline_y <= edge[1][1] or edge[1][1] <= scanline_y <= edge[0][1]: 
                    if abs(edge[1][0] - edge[0][0]) > 1 and abs(edge[1][1] - edge[0][1]) > 1: # No horizontal and vertical edge
                        gradient =  (edge[1][0] - edge[0][0]) / (edge[1][1] - edge[0][1])
                        intersect_x = edge[0][0] + (scanline_y - edge[0][1]) * gradient
                        intersections.append((intersect_x, scanline_y))
                    elif abs(edge[1][0] - edge[0][0]) < 1: # x is equal, hence vertical edge
                        intersections.append((edge[0][0], scanline_y))
                    elif abs(edge[1][1] - edge[0][1]) < 1: # y is equal, hence horizontal edge
                        intersections.append((edge[0][0], scanline_y))
                        intersections.append((edge[1][0], scanline_y))
                    

            intersections.sort(key=lambda x: x[0])
            # Remove duplicates
            for i in range(len(intersections) - 1):
                if abs(intersections[i+1][0] - intersections[i][0]) < 1 and abs(intersections[i+1][1] - intersections[i][1]) < 1:
                    intersections[i] = None
            intersections = [x for x in intersections if x is not None]

            scanned_lines.append(intersections)
            scanline_y += 3
            if scanline_y >= max_y and scanline_y - max_y < 3:
                scanline_y = max_y

        
        # Un-rotate the coordinates
        for line in scanned_lines:
            for i in range(len(line)):
                line[i] = rotate_point(line[i][0], line[i][1], -angle)

        jump_stitches = 0
        # Jump to start coordinate if needed
        if abs(Vec2D(scanned_lines[0][0][0], scanned_lines[0][0][1]) - turtle.pos()) > 1:
            with turtle.jump_stitch():
                jump_stitches += 1
                if not simulate: turtle.goto(scanned_lines[0][0])

        no_fill_in_current_iteration_flag = False
        while not no_fill_in_current_iteration_flag:
            no_fill_in_current_iteration_flag = True
            jump = False
            for i in range(len(scanned_lines) - 1):
                with turtle.direct_stitch():
                    if len(scanned_lines[i]) >= 2:
                        no_fill_in_current_iteration_flag = False
                        if jump: 
                            with turtle.jump_stitch():
                                if not simulate: turtle.goto(scanned_lines[i][0])
                                jump_stitches += 1
                                jump = False
                        if not simulate: turtle.goto(scanned_lines[i][0])
                        if not simulate: turtle.goto(scanned_lines[i][1])
                        scanned_lines[i].pop(0)
                        scanned_lines[i].pop(0)
                    else:
                        jump = True

        return jump_stitches
    
    def fill(self, turtle, points):
        if not self.auto:
            self._fill_at_angle(turtle, points, self.angle)
        else:
            best_angle = 0
            min_jumps = self._fill_at_angle(turtle, points, best_angle, simulate=True)
            for angle in (math.pi/4, math.pi/2, 3*math.pi/4):
                jumps = self._fill_at_angle(turtle, points, angle, simulate=True)
                if jumps < min_jumps:
                    min_jumps = jumps
                    best_angle = angle

            self._fill_at_angle(turtle, points, best_angle)

        

 
                        
                        
            