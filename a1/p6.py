import sys, parse, grader, copy

def number_of_attacks(problem):
    #Your p6 code here
    width = len(problem[0])
    height = len(problem)

    curr_width = 1
    curr_height = 1

    solution = ""
    while curr_height <= height:
        while curr_width <= width:

            num_height = 0
            while num_height < height:

                if (problem[num_height][curr_width - 1] == "q"):
                    prev_queen_height = num_height
                    break
                num_height += 1
            
            curr_problem = problem
            if (curr_height - 1 != prev_queen_height):
                curr_problem[curr_height - 1][curr_width - 1] = "q"
                curr_problem[prev_queen_height][curr_width - 1] = 0

            if curr_width < width:
                solution += str(attack_count(curr_problem)) + " "

            curr_width += 1
        if curr_height < height:
            solution += str(attack_count(curr_problem)) + "\n"
        else:
            solution += str(attack_count(curr_problem))
        curr_width = 1
        curr_height += 1

    return solution

def attack_count(problem):
    width = len(problem[0])
    height = len(problem)

    attack_count = 0

    # calculate by rows
    curr_width = 1
    curr_height = 1

    while curr_height <= height:
        row_count = 0
        while curr_width <= width:
            if problem[curr_height - 1][curr_width - 1] == "q":
                row_count += 1
            curr_width += 1
        attack_count += (1 + row_count - 1) * (row_count - 1) / 2
        curr_width = 1
        curr_height += 1

    # calculate by columns
    curr_width = 1
    curr_height = 1

    while curr_width <= width:
        column_count = 0
        while curr_height <= height:
            if problem[curr_height - 1][curr_width - 1] == "q":
                column_count += 1
            curr_height += 1
        attack_count += (1 + column_count - 1) * (column_count - 1) / 2
        curr_height = 1
        curr_width += 1

    # calculate by left diagonals
    curr_width = 1
    curr_height = height

    left_diagonal_count = 0
    while curr_width <= width:
        width_helper = curr_width
        while curr_height >= 1 and width_helper >= 1:
            if (problem[curr_height - 1][width_helper - 1] == "q"):
                left_diagonal_count += 1
            curr_height -= 1
            width_helper -= 1
        attack_count += (1 + left_diagonal_count - 1) * (left_diagonal_count - 1) / 2
        left_diagonal_count = 0
        curr_width += 1
        curr_height = height

    # calculate by right diagonals
    curr_width = width
    curr_height = height

    right_diagonal_count = 0
    while curr_width >= 1:
        width_helper = curr_width
        while curr_height >= 1 and width_helper <= width:
            if (problem[curr_height - 1][width_helper - 1] == "q"):
                right_diagonal_count += 1
            curr_height -= 1
            width_helper += 1
        attack_count += (1 + right_diagonal_count - 1) * (right_diagonal_count - 1) / 2
        right_diagonal_count = 0
        curr_width -= 1
        curr_height = height

    return int(attack_count)



if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -4
    problem_id = 6
    grader.grade(problem_id, test_case_id, number_of_attacks, parse.read_8queens_search_problem)