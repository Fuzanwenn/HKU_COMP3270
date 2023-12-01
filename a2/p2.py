import sys, random , parse
import time, os, copy
from p1 import get_ghost_loc, get_pacman_loc, get_foods_loc, get_next_loc, convert_map_to_str

def reflex_play_single_ghost(problem, verbose):
    #Your p2 code here
    seeds = problem[0]
    layout = problem[1]

    ghost_loc = get_ghost_loc(layout)
    pacman_loc = get_pacman_loc(layout)
    foods_loc = get_foods_loc(layout)

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
            next_direction = evaluate_direction(pacman_loc, ghost_loc, foods_loc, score, food_num)
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
                    foods_loc.remove([pacman_loc[0][0], pacman_loc[0][1] + 1])
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
                    foods_loc.remove([pacman_loc[0][0] - 1, pacman_loc[0][1]])
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
                    foods_loc.remove([pacman_loc[0][0] + 1, pacman_loc[0][1]])
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
                    foods_loc.remove([pacman_loc[0][0], pacman_loc[0][1] - 1])
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

    return solution, winner

def evalutaion_func(pacman_loc, ghost_loc, foods_loc, score, food_num):
    distance_to_ghost = abs(pacman_loc[0] - ghost_loc[0][0]) + abs(pacman_loc[1] - ghost_loc[0][1])
    nearest_food = nearest_foods(pacman_loc, foods_loc)
    distance_to_foods = abs(pacman_loc[0] - nearest_food[0]) + abs(pacman_loc[1] - nearest_food[1])
    value = score - 1.5 * distance_to_foods - 1.5 * (1/distance_to_ghost if distance_to_ghost != 0 else float('inf')) - 4 * food_num
    return value

def evaluate_direction(pacman_loc, ghost_loc, foods_loc, score, food_num):
    value_E = evalutaion_func([pacman_loc[0][0], pacman_loc[0][1] + 1], ghost_loc, foods_loc, score, food_num)
    value_N = evalutaion_func([pacman_loc[0][0] - 1, pacman_loc[0][1]], ghost_loc, foods_loc, score, food_num)
    value_S = evalutaion_func([pacman_loc[0][0] + 1, pacman_loc[0][1]], ghost_loc, foods_loc, score, food_num)
    value_W = evalutaion_func([pacman_loc[0][0], pacman_loc[0][1] - 1], ghost_loc, foods_loc, score, food_num)
    value_list = [value_E, value_N, value_S, value_W]
    max_value = max(value_list)
    if (max_value == value_E):
        return 'E'
    elif (max_value == value_N):
        return 'N'
    elif (max_value == value_S):
        return 'S'
    else:
        return 'W'

def nearest_foods(pacman_loc, foods_loc):
    shortest_distance = 10000
    for food in foods_loc:
        curr_distance = abs(pacman_loc[0] - food[0]) + abs(pacman_loc[1] - food[1])
        if curr_distance < shortest_distance:
            shortest_distance = curr_distance
            nearest_food = food
    return nearest_food

if __name__ == "__main__":
    #random.seed(0)
    test_case_id = int(sys.argv[1])    
    problem_id = 2
    file_name_problem = str(test_case_id)+'.prob' 
    file_name_sol = str(test_case_id)+'.sol'
    path = os.path.join('test_cases','p'+str(problem_id)) 
    problem = parse.read_layout_problem(os.path.join(path,file_name_problem))
    num_trials = int(sys.argv[2])
    verbose = bool(int(sys.argv[3]))
    print('test_case_id:',test_case_id)
    print('num_trials:',num_trials)
    print('verbose:',verbose)
    start = time.time()
    win_count = 0
    for i in range(num_trials):
        #print(i)
        solution, winner = reflex_play_single_ghost(copy.deepcopy(problem), verbose)
        if winner == 'Pacman':
            win_count += 1
        if verbose:
            print(solution)
    win_p = win_count/num_trials * 100
    end = time.time()
    print('time:',end - start)
    print('win %',win_p)