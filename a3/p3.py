import sys, grader, parse
from copy import deepcopy

def value_iteration(problem):
    discount = float(problem[0])
    noise = float(problem[1])
    livingReward = float(problem[2])
    iterations = int(problem[3])
    grid = problem[5]
    direction_grid = []

    return_value = 'V_k=0\n'

    return_value += print_formatted_grid(initialize(grid))

    return_value += 'V_k=1\n'
    grid = first_grid(grid, livingReward)
    print(grid)
    return_value += print_formatted_grid(grid)

    return_value += 'pi_k=1\n'
    direction_grid = update_direction_grid(grid)
    print(direction_grid)
    return_value += print_formatted_grid(direction_grid)

    k = 2

    # while k <= iterations:
    #     return_value += 'V_k=' + str(k) + '\n'
    #     grid =  

    return return_value

def initialize(grid):
    initial_grid = []
    for i in range(len(grid)):
        lines = []
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                lines.append(' ##### ')
            else:
                lines.append(0.00)
        initial_grid.append(lines)
    return initial_grid

def first_grid(grid, livingReward):
    first_grid = []
    for row in grid:
        lines = []
        for col in row:
            if col == '_' or col == 'S':
                lines.append(float(livingReward))
            elif col == '#':
                lines.append(' ##### ')
            else:
                lines.append(float(col))
        first_grid.append(lines)
    return first_grid

def update_direction_grid(grid):
    direction_grid = []
    for row in grid:
        result = []
        for col in row:
            if col == ' ##### ':
                result.append(' # ')
            else:
                result.append(' ' + get_direction(grid, row, col) + ' ')
        direction_grid.append(result)
    return direction_grid

def get_direction(grid, row, col):
    max = 0
    N_value = 0
    E_value = 0
    S_value = 0
    W_value = 0
    try:
        N_value = grid[row - 1][col]
    except:
        pass
    try:
        E_value = grid[row][col + 1]
    except:
        pass
    try:
        S_value = grid[row + 1][col]
    except:
        pass
    try:
        W_value = grid[row][col - 1]
    except:
        pass
    max = N_value
    direction = 'N'
    if E_value > max:
        max = E_value
        direction = 'E'
    if S_value > max:
        max = S_value
        direction = 'S'
    if W_value > max:
        max = W_value
        direction = 'W'
    return direction
        


def print_formatted_grid(grid):
    result = ''
    for row in grid:
        for col in row:
            if isinstance(col, float):
                result += "|{:7.2f}|".format(col)
            else:
                result += "|" + col + "|"
        result += '\n'
    return result

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -4
    problem_id = 3
    grader.grade(problem_id, test_case_id, value_iteration, parse.read_grid_mdp_problem_p3)