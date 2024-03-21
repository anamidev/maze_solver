import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols)
        self.assertEqual(
            m1._cells[0][0].has_wall_top,
            False
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_wall_bottom,
            False,
        )

if __name__ == "__main__":
    unittest.main()
