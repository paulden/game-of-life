import time

from game_of_life import main

INPUT_EXAMPLE = [[0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]


def pretty_print(grid):
    for row in grid:
        line = ''
        for cell in row:
            if cell == 0:
                line += ' . '
            else:
                line += ' x '
        print(line)


def main_loop(starting_grid, predict_func):
    time_step = 1

    pretty_print(starting_grid)
    current_grid = starting_grid

    while True:
        print('\n')
        current_grid = predict_func(current_grid)
        pretty_print(current_grid)
        time.sleep(time_step)


if __name__ == '__main__':
    pretty_print(INPUT_EXAMPLE)
