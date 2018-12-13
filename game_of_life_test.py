import unittest

from game_of_life import get_next_state


class GameOfLifeTest(unittest.TestCase):

    def setUp(self):
        self.empty_grid = [[0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0]]

    def test_that_an_empty_grid_should_return_an_empty_grid(self):
        # When
        actual = get_next_state(self.empty_grid)
        # Then
        self.assertEqual(self.empty_grid, actual)

    def test_that_a_grid_with_only_one_alive_cell_should_return_an_empty_grid(self):
        # Given
        input = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

        # When
        actual = get_next_state(input)

        # Then
        self.assertEqual(self.empty_grid, actual)

    def test_that_2x2_square_is_immutable(self):
        # Given
        input = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

        # When
        actual = get_next_state(input)

        # Then
        self.assertEqual(input, actual)

    def test_that_2x2_square_is_immutable_2(self):
        # Given
        input = [[0, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

        # When
        actual = get_next_state(input)

        # Then
        self.assertEqual(input, actual)

    def test_that_3_living_cells_should_create_a_new_cell(self):
        # Given
        input = [[0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

        expected = [[0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        # When
        actual = get_next_state(input)

        # Then
        self.assertEqual(expected, actual)

    def test_that_2_times_3_living_cells_should_create_two_cells(self):
        # Given
        input = [[0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0]]

        expected = [[0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]
        # When
        actual = get_next_state(input)

        # Then
        self.assertEqual(expected, actual)

    def test_that_if_cell_4_neighboors_it_dies(self):
        # Given
        input = [[0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

        # When
        actual = get_next_state(input)

        # Then
        self.assertEqual(0, actual[2][2])
