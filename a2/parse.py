import os, sys

def read_layout_problem(file_path):
    #Your p1 code here
    problem = []
    curr = []
    with open(file_path, 'r') as f:
        seeds = f.readline()[6:-1]
        while True:
            lines = f.read(1)
            if (lines == ''):
                problem.append(curr)
                break
            else:
                if (lines == '\n'):
                    problem.append(curr)
                    curr = []
                    continue
                else:
                    curr.append(lines)
    return [int(seeds), problem]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        problem = read_layout_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')