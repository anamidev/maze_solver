from point import Point

class Line():
    def __init__(self, point_start = Point(0,0), point_end = Point(0,0), win = None):
        self._win = win
        self.point_start = point_start
        self.point_end = point_end

    def draw(self, color):
        if self._win:
            self._win.canvas.create_line(self.point_start.x, self.point_start.y, self.point_end.x, self.point_end.y, fill=color, width=2)
            self._win.canvas.pack()