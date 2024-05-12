from createCNF import createCNFs
import copy

def solve_with_backtracking(puzzle_origin):
    puzzle=list(map(lambda row: [int(i) if i.isdigit() else i for i in row], puzzle_origin))
    clauses = createCNFs(puzzle)
    variables = list(set(abs(literal) for clause in clauses for literal in clause))
    assignments = [0] * len(variables)
    check = SAT_solver(clauses, variables, assignments, 0)
    m = len(puzzle[0])

    if check:
        for i in range(len(variables)):
            puzzle[(variables[i]) - 1 // m][(variables[i]) - 1 % m] = \
                                                                "T" if assignments[i] else "G"
        for i in range(len(puzzle)):
            for j in range(m):
                if puzzle[i][j] == "_":
                    puzzle[i][j] = "G"
    return check, puzzle


def unitPropagate(l,cnfs):
    i=0
    while i < len(cnfs):
        #xóa các clause chứa biến l vì nó đã đúng sẵn rồi
        if l in cnfs[i]:
            cnfs.pop(i) 
            continue

        #xóa các biến -l trong các mệnh đề đó vì l đúng 
        #thì -l sai nó k có ý nghĩa trong các mệnh đề khác
        if (-l) in cnfs[i]:
            cnfs[i].remove(-l)
        i+=1


def SAT_solver(clauses, variables, assignments, k):
    if clauses == []:
        return True
    elif [] in clauses:
        return False
        
    for i in [True, False]:
        assignments[k] = i
        cnfs = copy.deepcopy(clauses)
        unitPropagate((1 if i else - 1) * variables[k], cnfs)
        if SAT_solver(cnfs, variables, assignments, k + 1):
            return True
        assignments[k] = 0
    return False
