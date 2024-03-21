import time
import random
from point import Point
from line import Line
from cell import Cell

class Maze():
    def __init__(self, x1 = 0, y1 = 0, num_rows = 2, num_cols = 2, cell_size_x = 16, cell_size_y = 16, win = None, seed = None):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        row_x = self._x1
        row_y = self._y1

        for _ in range(self._num_rows):
            col = []
            col_x = row_x
            col_y = row_y
            for _ in range(self._num_cols):
                col.append(Cell(Point(col_x, col_y), Point(col_x + self._cell_size_x, col_y + self._cell_size_y), self._win))
                col_x += self._cell_size_x
            self._cells.append(col)
            row_y += self._cell_size_y

            
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win:
            self._cells[i][j].draw("blue")
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(2 / 100)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_wall_top = False
        self._draw_cell(0,0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_wall_bottom = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return

            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_wall_bottom = False
                self._cells[i + 1][j].has_wall_top = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_wall_top = False
                self._cells[i - 1][j].has_wall_bottom = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_wall_right = False
                self._cells[i][j + 1].has_wall_left = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_wall_left = False
                self._cells[i][j - 1].has_wall_right = False

            self._break_walls(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        if (
            j > 0
            and not self._cells[i][j].has_wall_left
            and not self._cells[i][j - 1].visited
        ):
            self._win.draw_move(self._cells[i][j], self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._win.draw_move(self._cells[i][j], self._cells[i][j - 1], True)

        if (
            j < self._num_cols - 1
            and not self._cells[i][j].has_wall_right
            and not self._cells[i][j + 1].visited
        ):
            self._win.draw_move(self._cells[i][j], self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._win.draw_move(self._cells[i][j], self._cells[i][j + 1], True)

        if (
            i > 0
            and not self._cells[i][j].has_wall_top
            and not self._cells[i - 1][j].visited
        ):
            self._win.draw_move(self._cells[i][j], self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._win.draw_move(self._cells[i][j], self._cells[i - 1][j], True)

        if (
            i < self._num_rows - 1
            and not self._cells[i][j].has_wall_bottom
            and not self._cells[i + 1][j].visited
        ):
            self._win.draw_move(self._cells[i][j], self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._win.draw_move(self._cells[i][j], self._cells[i + 1][j], True)

        return False
        
