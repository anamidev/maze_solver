from tkinter import Tk, BOTH, Canvas
from line import Line
from maze import Maze

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.canvas = Canvas(self.__root, height=height, width=width, bg="white")
        self.canvas.pack()
        self.isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)
    
    def draw_cell(self, cell, color):
        cell.draw(self.canvas, color)

    def draw_move(self, from_cell, to_cell, undo=False):
        Line(from_cell.get_center(), to_cell.get_center(), self).draw("gray" if undo else "red")

def main():
    win = Window(800,800)
    maze = Maze(16, 16, 12, 12, 48, 48, win)
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()