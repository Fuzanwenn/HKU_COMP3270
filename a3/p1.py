import sys, random, grader, parse
from copy import deepcopy

def play_episode(problem):
    seed = int(problem[0])
    noise = float(problem[1])
    livingReward = float(problem[2])
    start_position = problem[3]
    curr_row = problem[3][0]
    curr_col = problem[3][1]
    grid = problem[4]
    policy = problem[5]
    cumulative_reward = 0
    grid[curr_row][curr_col] = 'P'
    result = ''
    result += initialize(grid)

    if seed!=-1:
        random.seed(seed, version=1)
    noise_direction = {'N':['N', 'E', 'W'], 'E':['E', 'S', 'N'], 'S':['S', 'W', 'E'], 'W':['W', 'N', 'S']}

    while True:
        intended_action = policy[curr_row][curr_col]

        if (intended_action == 'exit'):
            grid[curr_row][curr_col] = reward
            result += exit(reward, grid)
            cumulative_reward += reward
            cumulative_reward = round(cumulative_reward, 3)
            result += 'Cumulative reward sum: ' + str(cumulative_reward)
            break

        # To get the real action that it takes.
        actual_action = random.choices(population=noise_direction[intended_action], weights=[1 - noise*2, noise, noise])[0]

        result += 'Taking action: ' + actual_action + ' (intended: ' + intended_action + ')' + '\n'

        # To get the reward and the new position.
        act_result = take_action(curr_row, curr_col, start_position, grid, actual_action, livingReward)
        reward = act_result[0]
        curr_row = act_result[1]
        curr_col = act_result[2]
        
        result += 'Reward received: ' + str(livingReward) + '\n'
        result += 'New state:' + '\n'
        result += printGrid(grid)
        cumulative_reward += livingReward
        cumulative_reward = round(cumulative_reward, 3)
        result += 'Cumulative reward sum: ' + str(cumulative_reward) + '\n'
        result += '-------------------------------------------- \n'

    with open('output.txt', 'w') as f:
        f.write(result)
    return result

# Initialize the first grid.
def initialize(grid):
    result = ''
    result += 'Start state:' + '\n'
    r = ''
    for row in grid:
        r += '    '
        col_num = 1
        for col in row:
            try:
                a = int(col)
                if (int(col) < 0):
                    r = r[:-1]
            except:
                pass
            if (col_num == len(row)):
                length = len(str(col))
                if length > 1:
                    if int(col) > 0:
                        r = r[:-length+1]
                    elif len(str(col)) > 2:
                        r = r[:-length+2]
                r += str(col) + '\n'
            else:
                length = len(str(col))
                if length > 1:
                    if int(col) > 0:
                        r = r[:-length+1]
                    elif len(str(col)) > 2:
                        r = r[:-length+2]
                r += str(col) + '    '
                col_num += 1
    result += r[0:-1] + '\n'
    result += 'Cumulative reward sum: 0.0' + '\n'
    result += '-------------------------------------------- \n'
    return result

# Take action and return the reward and the new position.
def take_action(curr_row, curr_col, start_position, grid, action, livingReward):
    next_item = ''
    if (action == 'N'):
        if (curr_row - 1 < 0):
            return [livingReward, curr_row, curr_col]
        next_item = grid[curr_row - 1][curr_col]
        if (next_item == '#'):
            return [livingReward, curr_row, curr_col]
        if (curr_row == start_position[0] and curr_col == start_position[1]):
            grid[curr_row][curr_col] = 'S'
        else:
            grid[curr_row][curr_col] = '_'
        curr_row -= 1
        
    elif (action == 'S'):
        if (curr_row + 1 >= len(grid)):
            return [livingReward, curr_row, curr_col]
        next_item = grid[curr_row + 1][curr_col]
        if (next_item == '#'):
            return [livingReward, curr_row, curr_col]
        if (curr_row == start_position[0] and curr_col == start_position[1]):
            grid[curr_row][curr_col] = 'S'
        else:
            grid[curr_row][curr_col] = '_'
        curr_row += 1
    
    elif (action == 'E'):
        if (curr_col + 1 >= len(grid[0])):
            return [livingReward, curr_row, curr_col]
        next_item = grid[curr_row][curr_col + 1]
        if (next_item == '#'):
            return [livingReward, curr_row, curr_col]
        if (curr_row == start_position[0] and curr_col == start_position[1]):
            grid[curr_row][curr_col] = 'S'
        else:
            grid[curr_row][curr_col] = '_'
        curr_col += 1
    
    elif (action == 'W'):
        if (curr_col - 1 < 0):
            return [livingReward, curr_row, curr_col]
        next_item = grid[curr_row][curr_col - 1]
        if (next_item == '#'):
            return [livingReward, curr_row, curr_col]
        if (curr_row == start_position[0] and curr_col == start_position[1]):
            grid[curr_row][curr_col] = 'S'
        else:
            grid[curr_row][curr_col] = '_'
        curr_col -= 1

    grid[curr_row][curr_col] = 'P'

    try:
        a = int(next_item)
        return [int(next_item), curr_row, curr_col]
    except:    
        return [livingReward, curr_row, curr_col]

# Exit the game.
def exit(reward, initial_grid):
    result = ''
    result += 'Taking action: exit (intended: exit)' + '\n'
    result += 'Reward received: ' + str(float(reward)) + '\n'
    result += 'New state:' + '\n'
    result += printGrid(initial_grid)
    return result

# Print the grid.
def printGrid(grid):
    r = ''
    for row in grid:
        r += '    '
        col_num = 1
        for col in row:
            try:
                a = int(col)
                if (int(col) < 0):
                    r = r[:-1]
            except:
                pass
            if (col_num == len(row)):
                length = len(str(col))
                if length > 1:
                    if int(col) > 0:
                        r = r[:-length+1]
                    elif len(str(col)) > 2:
                        r = r[:-length+2]
                r += str(col) + '\n'
            else:
                length = len(str(col))
                if length > 1:
                    if int(col) > 0:
                        r = r[:-length+1]
                    elif len(str(col)) > 2:
                        r = r[:-length+2]
                r += str(col) + '    '
                col_num += 1
    return r[0:-1] + '\n'

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -8
    problem_id = 1
    grader.grade(problem_id, test_case_id, play_episode, parse.read_grid_mdp_problem_p1)