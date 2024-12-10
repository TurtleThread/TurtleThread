from abc import ABC, abstractmethod

class Fill(ABC):
    """A class to represent a fill. This is a base class for other fill types.
    Given a list of points that make up a polygon, the fill() function should fill it in using the appropriate methods."""

    @abstractmethod
    def fill(self, points):
        raise NotImplementedError

class ScanlineFill(Fill):
    def __init__(self, angle):
        self.angle = angle

    def fill(self, turtle, points):
        # Basic scanline fill implementation, scanning left to right
        edges = []
        min_y = points[0][1]
        max_y = points[0][1]
        for i in range(len(points) - 1):
            edges.append((points[i], points[i + 1]))
            min_y = min(min_y, points[i + 1][1])
            max_y = max(max_y, points[i + 1][1])

        scanline_y = min_y
        scanned_lines = []
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
                                turtle.goto(scanned_lines[i][0])
                                jump = False
                        turtle.goto(scanned_lines[i][0])
                        turtle.goto(scanned_lines[i][1])
                        scanned_lines[i].pop(0)
                        scanned_lines[i].pop(0)
                    else:
                        jump = True
                        
                        
            