from line import Line
from point import Point

class Cell():
    def __init__(self, point_tl = Point(0,0), point_br = Point(0,0), win = None):
        self._win = win
        self._point_tl = point_tl
        self._point_br = point_br
        self._point_tr = Point(self._point_br.x, self._point_tl.y)
        self._point_bl = Point(self._point_tl.x, self._point_br.y)

        self.has_wall_left = True
        self.has_wall_top = True
        self.has_wall_right = True
        self.has_wall_bottom = True
        self.visited = False

    def draw(self, color):
        Line(self._point_tl, self._point_bl, self._win).draw(color if self.has_wall_left else "white")
        Line(self._point_tl, self._point_tr, self._win).draw(color if self.has_wall_top else "white")
        Line(self._point_tr, self._point_br, self._win).draw(color if self.has_wall_right else "white")
        Line(self._point_bl, self._point_br, self._win).draw(color if self.has_wall_bottom else "white")

    def get_center(self):
        x = (self._point_tl.x + self._point_tr.x) // 2
        y = (self._point_tl.y + self._point_bl.y) // 2
        return Point(x,y)