import unittest
from src.lab3 import sudoku


class SudokuTestCase(unittest.TestCase):

    def setUp(self):
        """
        Этот метод выполняется ПЕРЕД КАЖДЫМ тестом.
        Он загружает чистую доску, чтобы тесты не влияли друг на друга.
        """

        self.grid = sudoku.read_sudoku('src/lab3/puzzle1.txt')

    def test_group(self):
        self.assertEqual(sudoku.group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(sudoku.group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_row(self):
        grid_3x3 = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(sudoku.get_row(grid_3x3, (0, 0)), ['1', '2', '.'])
        self.assertEqual(sudoku.get_row(grid_3x3, (1, 0)), ['4', '5', '6'])

    def test_get_col(self):
        grid_3x3 = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(sudoku.get_col(grid_3x3, (0, 0)), ['1', '4', '7'])
        self.assertEqual(sudoku.get_col(grid_3x3, (0, 1)), ['2', '5', '8'])

    def test_get_block(self):
        self.assertEqual(sudoku.get_block(self.grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(sudoku.get_block(self.grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])

    def test_find_empty_positions(self):
        grid_3x3 = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(sudoku.find_empty_positions(grid_3x3), (0, 2))

    def test_find_possible_values(self):
        values = sudoku.find_possible_values(self.grid, (0, 2))
        self.assertEqual(values, {'1', '2', '4'})

        values = sudoku.find_possible_values(self.grid, (4, 7))
        self.assertEqual(values, {'2', '5', '9'})

    def test_solve(self):
        solution = sudoku.solve(self.grid)
        self.assertIsNotNone(solution)
        self.assertTrue(sudoku.check_solution(solution))


if __name__ == '__main__':
    unittest.main()