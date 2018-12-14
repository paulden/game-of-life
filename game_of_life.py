from copy import deepcopy


def get_next_state(input_grid):
    count = 0
    result_grid = deepcopy(input_grid)
    for index_row, row in enumerate(input_grid):
        for index_column, cell in enumerate(row):
            count += cell
            nb_alive_neighboors = get_number_of_alive_neighboors(index_column, index_row, input_grid)

            if cell == 0 and nb_alive_neighboors == 3:
                result_grid[index_row][index_column] = 1

            if cell == 1 and nb_alive_neighboors >= 4:
                result_grid[index_row][index_column] = 0

            if cell == 1 and nb_alive_neighboors <= 1:
                result_grid[index_row][index_column] = 0

    return result_grid


def get_cell_value(index_row, index_column, input_grid):
    if index_row < 0 or index_row > 5 or index_column < 0 or index_column > 5:
        return 0

    return input_grid[index_row][index_column]


def get_number_of_alive_neighboors(index_column, index_row, input_grid):
    number_alive_neighboors = 0
    number_alive_neighboors += get_cell_value(index_row - 1, index_column - 1, input_grid)
    number_alive_neighboors += get_cell_value(index_row - 1, index_column, input_grid)
    number_alive_neighboors += get_cell_value(index_row - 1, index_column + 1, input_grid)
    number_alive_neighboors += get_cell_value(index_row, index_column - 1, input_grid)
    number_alive_neighboors += get_cell_value(index_row, index_column + 1, input_grid)
    number_alive_neighboors += get_cell_value(index_row + 1, index_column - 1, input_grid)
    number_alive_neighboors += get_cell_value(index_row + 1, index_column, input_grid)
    number_alive_neighboors += get_cell_value(index_row + 1, index_column + 1, input_grid)

    return number_alive_neighboors
