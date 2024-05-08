import itertools
# from pysat.formula import CNF
# from pysat.solvers import Solver

def main():
    puzzle = [
        [2, "_", "_",1, "_"],
        ["_", 5,4,2,"_"],
        [ 3,"_","_", 2,1],
        [3,"_",6,"_",1],
        [2,"_","_",2,1]
    ]
    puzzle=[
        [2,"_"],
        ["_",2],
        ["_","_"]
    ]
    puzzle=[
        [2,"_","_",1,"_"],
        ["_",5,4,2,"_"],
        [3,"_","_",2,1],
        [3,"_",7,"_",1],
        [2,"_","_",2,1]
    ]
    puzzle=[
        [3,"_",2],
        ["_","_",2],
        ["_",3,1],
    ]
    m = len(puzzle[0])
    clauses = []
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != "_":
                clauses += pointCNF(puzzle, i, j)
    print(clauses)           
    # cnf = CNF(from_clauses=clauses)
    # with Solver(bootstrap_with=cnf) as solver:
    #     if solver.solve():
    #         result = solver.get_model()
    # result = [result[i] + (- 1 if result[i] > 0 else 1)  for i in range(1, len(result))]
    # print(result)
"""
    for i in result:
        if i > 0:
   """         
    

def pointCNF(p, r, c): #puzzle, row, column are considered
    n = len(p) #number of rows
    m = len(p[r]) #number of columns
    atomic = []
    for i in range(max(0, r - 1), min(r + 2, n)):
        for j in range(max(0, c - 1), min(c + 2, m)):
            if p[i][j] == "_":
               atomic.append(m*i + j + 1) #add index of p[i][j] in row-major order

    cnf = []

    for i in range(len(atomic)+1):
        if i != p[r][c]:
            cnf += list(itertools.combinations(atomic, i))  

    for i in range(len(cnf)):
        cnf[i] = [*cnf[i]]

    for i in atomic:
        for j in cnf:
            if i not in j:
                j.append(-i)
    for i in cnf:
        for j in range(len(i)):
            i[j] = -i[j]
            
    return cnf

if __name__ == "__main__":
    main()
