from copy import deepcopy


def get_next_state(grid):
    next_grid = deepcopy(grid)
    height = len(grid)
    width = len(grid[0])

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            living_neighbors = compute_living_neighbors(grid, i, j, height, width)

            if cell == 0:
                if living_neighbors == 3:
                    next_grid[i][j] = 1
            else:
                if living_neighbors <= 1 or living_neighbors >= 4:
                    next_grid[i][j] = 0
                if 2 <= living_neighbors <= 3:
                    next_grid[i][j] = 1

    return next_grid


def compute_living_neighbors(grid, i, j, height, width):
    living_neighbors = 0

    for neighbor_i in range(max(0, i - 1), min(height, i + 2)):
        for neighbor_j in range(max(0, j - 1), min(width, j + 2)):
            living_neighbors += grid[neighbor_i][neighbor_j]

    return living_neighbors - grid[i][j]
