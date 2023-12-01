
def read_grid_mdp_problem_p1(file_path):
    #Your p1 code here
    grid = []
    policy = []
    lines = []
    row_num = 0
    col_num = 0
    with open (file_path, 'r') as f:
        seed = f.readline()[6:-1]
        noise = f.readline()[7:-1]
        livingReward = f.readline()[14:-1]
        f.readline()
        while True: 
            curr = f.read(1)
            if (curr == 'p' or curr == 'o'):
                f.readline()
                break
            if (curr == '\n'):
                grid.append(lines)
                lines = []
                row_num += 1
                col_num = 0
                continue
            if (curr == ' '):
                continue
            if (curr == '-'):
                r = '-'
                curr = f.read(1)
                while (curr != ' ' and curr != '\n'):
                    r += curr
                    curr = f.read(1)
                lines.append(r)
                col_num += 1
                if (curr == '\n'):
                    grid.append(lines)
                    lines = []
                    row_num += 1
                    col_num = 0
                continue
            if (curr == 'S'):
                position = [row_num, col_num]
                lines.append(curr)
                col_num += 1
                continue
            if (curr == '_' or curr == '#'):
                lines.append(curr)
                col_num += 1
                continue
            else:
                r = curr
                curr = f.read(1)
                while (curr != ' ' and curr != '\n'):
                    r += curr
                    curr = f.read(1)
                lines.append(r)
                col_num += 1
                if (curr == '\n'):
                    grid.append(lines)
                    lines = []
                    row_num += 1
                    col_num = 0
                continue

        lines = []
        while True:
            curr = f.read(1)
            if (curr == '\n'):
                policy.append(lines)
                lines = []
                continue
            if (curr == ' '):
                continue
            if (curr == ''):
                policy.append(lines)
                break
            if (curr == 'e'):
                lines.append('exit')
                f.read(3)
                continue
            lines.append(curr)

    return [seed, noise, livingReward, position, grid, policy]

def read_grid_mdp_problem_p2(file_path):
    #Your p2 code here
    grid = []
    policy = []
    lines = []
    row_num = 0
    col_num = 0
    with open (file_path, 'r') as f:
        discount = f.readline()[10:-1]
        noise = f.readline()[7:-1]
        livingReward = f.readline()[14:-1]
        iterations = f.readline()[12:-1]
        f.readline()
        while True: 
            curr = f.read(1)
            if (curr == 'p' or curr == 'o'):
                f.readline()
                break
            if (curr == '\n'):
                grid.append(lines)
                lines = []
                row_num += 1
                col_num = 0
                continue
            if (curr == ' '):
                continue
            if (curr == '-'):
                r = '-'
                curr = f.read(1)
                while (curr != ' ' and curr != '\n'):
                    r += curr
                    curr = f.read(1)
                lines.append(r)
                col_num += 1
                if (curr == '\n'):
                    grid.append(lines)
                    lines = []
                    row_num += 1
                    col_num = 0
                continue
            if (curr == 'S'):
                position = [row_num, col_num]
                lines.append(curr)
                col_num += 1
                continue
            if (curr == '_' or curr == '#'):
                lines.append(curr)
                col_num += 1
                continue
            else:
                r = curr
                curr = f.read(1)
                while (curr != ' ' and curr != '\n'):
                    r += curr
                    curr = f.read(1)
                lines.append(r)
                col_num += 1
                if (curr == '\n'):
                    grid.append(lines)
                    lines = []
                    row_num += 1
                    col_num = 0
                continue

        lines = []
        while True:
            curr = f.read(1)
            if (curr == '\n'):
                policy.append(lines)
                lines = []
                continue
            if (curr == ' '):
                continue
            if (curr == ''):
                policy.append(lines)
                break
            if (curr == 'e'):
                lines.append('exit')
                f.read(3)
                continue
            lines.append(curr)

    return [discount, noise, livingReward, iterations, position, grid, policy]

def read_grid_mdp_problem_p3(file_path):
    #Your p3 code here
    grid = []
    lines = []
    row_num = 0
    col_num = 0
    with open (file_path, 'r') as f:
        discount = f.readline()[10:-1]
        noise = f.readline()[7:-1]
        livingReward = f.readline()[14:-1]
        iterations = f.readline()[12:-1]
        f.readline()
        while True: 
            curr = f.read(1)
            if (curr == ''):
                grid.append(lines)
                break
            if (curr == '\n'):
                grid.append(lines)
                lines = []
                row_num += 1
                col_num = 0
                continue
            if (curr == ' '):
                continue
            if (curr == '-'):
                r = '-'
                curr = f.read(1)
                while (curr != ' ' and curr != '\n'):
                    r += curr
                    curr = f.read(1)
                lines.append(r)
                col_num += 1
                if (curr == '\n'):
                    grid.append(lines)
                    lines = []
                    row_num += 1
                    col_num = 0
                continue
            if (curr == 'S'):
                position = [row_num, col_num]
                lines.append(curr)
                col_num += 1
                continue
            if (curr == '_' or curr == '#'):
                lines.append(curr)
                col_num += 1
                continue
            else:
                r = curr
                curr = f.read(1)
                while (curr != ' ' and curr != '\n'):
                    r += curr
                    curr = f.read(1)
                lines.append(r)
                col_num += 1
                if (curr == '\n'):
                    grid.append(lines)
                    lines = []
                    row_num += 1
                    col_num = 0
                continue
    return [discount, noise, livingReward, iterations, position, grid]

def read_grid_mdp_problem_p4(file_path):
    #Your p4 code here
    problem = ''
    return problem