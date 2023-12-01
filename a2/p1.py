import sys, random, grader, parse

def random_play_single_ghost(problem):
    #Your p1 code here
    seeds = problem[0]
    layout = problem[1]
    
    ghost_loc = get_ghost_loc(layout)
    pacman_loc = get_pacman_loc(layout)
    foods_loc = get_foods_loc(layout)

    random.seed(seeds, 1)
    solution = 'seed: ' + str(seeds) + '\n'
    solution += '0\n' + convert_map_to_str(layout)
    steps_count = 0
    is_pacman_moving = True
    food_num = len(foods_loc)
    score = 0
    ghost_is_on_food = False

    while True:
        steps_count += 1
        if (is_pacman_moving):
            score += -1
            next_available_direction = get_next_loc(pacman_loc, layout)
            next_direction = random.choice(tuple(next_available_direction))
            solution += str(steps_count) + ': P moving ' + str(next_direction) + '\n'
            if (next_direction == 'E'):
                next_item = layout[pacman_loc[0][0]][pacman_loc[0][1] + 1]
                if (next_item == 'W'):
                    score += -500
                    winner = 'Ghost'
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] + 1] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] + 1] = 'P'
                    pacman_loc[0][1] += 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break                      
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] + 1] = 'P'
                    pacman_loc[0][1] += 1

            elif (next_direction == 'N'):
                next_item = layout[pacman_loc[0][0] - 1][pacman_loc[0][1]]
                if (next_item == 'W'):
                    score += -500
                    winner = 'Ghost'
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] - 1][pacman_loc[0][1]] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] - 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] -= 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] - 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] -= 1

            elif (next_direction == 'S'):
                next_item = layout[pacman_loc[0][0] + 1][pacman_loc[0][1]]
                if (next_item == 'W'):
                    score += -500
                    winner = 'Ghost'
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] + 1][pacman_loc[0][1]] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] + 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] += 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] + 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] += 1
            
            elif (next_direction == 'W'):
                next_item = layout[pacman_loc[0][0]][pacman_loc[0][1] - 1]
                if (next_item == 'W'):
                    score += -500
                    winner = 'Ghost'
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] - 1] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] - 1] = 'P'
                    pacman_loc[0][1] -= 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] - 1] = 'P'
                    pacman_loc[0][1] -= 1
            is_pacman_moving = False
            solution += convert_map_to_str(layout)
            solution += 'score: ' + str(score) + '\n'

        # Ghost moving
        else:
            next_available_direction = get_next_loc(ghost_loc, layout)
            next_direction = random.choice(tuple(next_available_direction))
            solution += str(steps_count) + ': W moving ' + str(next_direction) + '\n'
            if (next_direction == 'E'):
                next_item = layout[ghost_loc[0][0]][ghost_loc[0][1] + 1]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    layout[ghost_loc[0][0]][ghost_loc[0][1] + 1] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                        ghost_is_on_food = True
                    curr_food = [ghost_loc[0][0], ghost_loc[0][1] + 1]
                    layout[ghost_loc[0][0]][ghost_loc[0][1] + 1] = 'W'
                    ghost_loc[0][1] += 1
                else:
                    layout[ghost_loc[0][0]][ghost_loc[0][1] + 1] = 'W'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                        ghost_is_on_food = False
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    ghost_loc[0][1] += 1
            
            elif (next_direction == 'N'):
                next_item = layout[ghost_loc[0][0] - 1][ghost_loc[0][1]]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    layout[ghost_loc[0][0] - 1][ghost_loc[0][1]] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                        ghost_is_on_food = True
                    curr_food = [ghost_loc[0][0] - 1, ghost_loc[0][1]]
                    layout[ghost_loc[0][0] - 1][ghost_loc[0][1]] = 'W'
                    ghost_loc[0][0] -= 1
                else:
                    layout[ghost_loc[0][0] - 1][ghost_loc[0][1]] = 'W'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                        ghost_is_on_food = False
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    ghost_loc[0][0] -= 1
            
            elif (next_direction == 'S'):
                next_item = layout[ghost_loc[0][0] + 1][ghost_loc[0][1]]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    layout[ghost_loc[0][0] + 1][ghost_loc[0][1]] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                        ghost_is_on_food = True
                    curr_food = [ghost_loc[0][0] + 1, ghost_loc[0][1]]
                    layout[ghost_loc[0][0] + 1][ghost_loc[0][1]] = 'W'
                    ghost_loc[0][0] += 1
                else:
                    layout[ghost_loc[0][0] + 1][ghost_loc[0][1]] = 'W'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                        ghost_is_on_food = False
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    ghost_loc[0][0] += 1
            
            elif (next_direction == 'W'):
                next_item = layout[ghost_loc[0][0]][ghost_loc[0][1] - 1]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    layout[ghost_loc[0][0]][ghost_loc[0][1] - 1] = 'W'
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                        ghost_is_on_food = True
                    curr_food = [ghost_loc[0][0], ghost_loc[0][1] - 1]
                    layout[ghost_loc[0][0]][ghost_loc[0][1] - 1] = 'W'
                    ghost_loc[0][1] -= 1
                else:
                    layout[ghost_loc[0][0]][ghost_loc[0][1] - 1] = 'W'
                    if (ghost_is_on_food):
                        layout[curr_food[0]][curr_food[1]] = '.'
                        ghost_is_on_food = False
                    else:
                        layout[ghost_loc[0][0]][ghost_loc[0][1]] = ' '
                    ghost_loc[0][1] -= 1
                    
            is_pacman_moving = True
            solution += convert_map_to_str(layout)
            solution += 'score: ' + str(score) + '\n'

    return solution

def get_ghost_loc(layout):
    loc = []
    row = 0
    for rows in layout:
        col = 0
        for cols in rows:
            if (cols == 'W'):
                loc.append([row, col])
            col += 1
        row += 1
    return loc

def get_pacman_loc(layout):
    loc = []
    row = 0
    for rows in layout:
        col = 0
        for cols in rows:
            if (cols == 'P'):
                loc.append([row, col])
            col += 1
        row += 1
    return loc

def get_foods_loc(layout):
    loc = []
    row = 0
    for rows in layout:
        col = 0
        for cols in rows:
            if (cols == '.'):
                loc.append([row, col])
            col += 1
        row += 1
    return loc

def get_next_loc(loc, layout):
    row = loc[0][0]
    col = loc[0][1]
    direction = []
    if (layout[row][col + 1] != '%'):
        direction.append('E')
    if (layout[row - 1][col] != '%'):
        direction.append('N')
    if (layout[row + 1][col] != '%'):
        direction.append('S')
    if (layout[row][col - 1] != '%'):
        direction.append('W')
    return direction

def convert_map_to_str(layout):
    str = ''
    for rows in layout:
        for cols in rows:
            str += cols
        str += '\n'
    return str

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -6
    problem_id = 1
    grader.grade(problem_id, test_case_id, random_play_single_ghost, parse.read_layout_problem) 