import sys, grader, parse
from copy import deepcopy

def policy_evaluation(problem):
    discount = float(problem[0])
    noise = float(problem[1])
    livingReward = float(problem[2])
    iterations = int(problem[3])
    grid = problem[5]
    policy = problem[6]
    k = 2

    return_value = 'V^pi_k=0\n'
    return_value += print_formatted_grid(initialize(grid))
    return_value += 'V^pi_k=1\n'
    grid = first_grid(grid, livingReward)
    return_value += print_formatted_grid(grid)

    # Iteratively update the grid within the number of iterations.
    while k <= iterations - 1:
        return_value += 'V^pi_k=' + str(k) + '\n'
        curr_grid = deepcopy(grid)
        for curr_row in range(len(grid)):
            for curr_col in range(len(grid[0])):
                value = policy_evaluation_helper(grid, policy, discount, noise, livingReward, curr_row, curr_col)
                if value == 1000000000:
                    curr_grid[curr_row][curr_col] = '#'
                else:
                    curr_grid[curr_row][curr_col] = policy_evaluation_helper(grid, policy, discount, noise, livingReward, curr_row, curr_col)
        grid = deepcopy(curr_grid)
        return_value += print_formatted_grid(grid)
        k += 1

    with open('output.txt', 'w') as f:
        f.write(return_value[:-1])
    return return_value[:-1]

# Initialize the grid.
def initialize(grid):
    initial_grid = []
    for i in range(len(grid)):
        lines = []
        for j in range(len(grid[0])):
            lines.append(0.00)
        initial_grid.append(lines)
    return initial_grid

# Get the first step's grid.
def first_grid(grid, livingReward):
    first_grid = []
    for row in grid:
        lines = []
        for col in row:
            if col == '_' or col == '#' or col == 'S':
                lines.append(float(livingReward))
            else:
                lines.append(float(col))
        first_grid.append(lines)
    return first_grid

# Calculate the value of the current state.
def policy_evaluation_helper(grid, policy, discount, noise, livingReward, curr_row, curr_col):
    noise_direction = {'N':['N', 'E', 'W'], 'E':['E', 'S', 'N'], 'S':['S', 'W', 'E'], 'W':['W', 'N', 'S']}
    direction = {'N':[-1, 0], 'E':[0, 1], 'S':[1, 0], 'W':[0, -1]}
    intended_direction = policy[curr_row][curr_col]
    if intended_direction == 'exit':
        return grid[curr_row][curr_col]
    if intended_direction == '#':
        return 1000000000
    try:
        evaluation_value = (1 - 2 * noise) * (livingReward + discount * grid[curr_row + direction[intended_direction][0]][curr_col + direction[intended_direction][1]]) + noise * (livingReward + discount * grid[curr_row + direction[noise_direction[intended_direction][1]][0]][curr_col + direction[noise_direction[intended_direction][1]][1]]) + noise * (livingReward + discount * grid[curr_row + direction[noise_direction[intended_direction][2]][0]][curr_col + direction[noise_direction[intended_direction][2]][1]])
    except:
        try:
            evaluation_value = (1 - 2 * noise) * (livingReward + discount * grid[curr_row + direction[intended_direction][0]][curr_col + direction[intended_direction][1]]) + noise * (livingReward + discount * grid[curr_row + direction[noise_direction[intended_direction][1]][0]][curr_col + direction[noise_direction[intended_direction][1]][1]]) + noise * (livingReward + discount * grid[curr_row][curr_col])
        except:
            try:
                evaluation_value = (1 - 2 * noise) * (livingReward + discount * grid[curr_row + direction[intended_direction][0]][curr_col + direction[intended_direction][1]]) + noise * (livingReward + discount * grid[curr_row + direction[noise_direction[intended_direction][2]][0]][curr_col + direction[noise_direction[intended_direction][2]][1]]) + noise * (livingReward + discount * grid[curr_row][curr_col])
            except:
                evaluation_value = (1 - 2 * noise) * (livingReward + discount * grid[curr_row + direction[intended_direction][0]][curr_col + direction[intended_direction][1]]) + 2 * noise * (livingReward + discount * grid[curr_row][curr_col])
    return round(evaluation_value, 3)

# Print the grid.
def print_formatted_grid(grid):
    result = ''
    for row in grid:
        for col in row:
            if isinstance(col, float):
                result += "|{:7.2f}|".format(col)
            else:
                result += "| ##### |"
        result += '\n'
    return result
        

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -7
    problem_id = 2
    grader.grade(problem_id, test_case_id, policy_evaluation, parse.read_grid_mdp_problem_p2)