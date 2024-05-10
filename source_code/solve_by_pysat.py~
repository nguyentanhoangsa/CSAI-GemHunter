import copy
from createCNF import *
from pysat.formula import CNF
from pysat.solvers import Solver

def solveByPysat(puzzle_origin):
    puzzle=list(map(lambda row: [int(i) if i.isdigit() else i for i in row], puzzle_origin))
    clauses = createCNFs(puzzle)
    cnf = CNF(from_clauses=clauses)
    check = False
    result = None
    
    with Solver(bootstrap_with=cnf) as solver:
        check = solver.solve()
        if check:
            result = solver.get_model()
            
    newPuzzle = copy.deepcopy(puzzle)
    if result:
        n = len(newPuzzle)
        m = len(newPuzzle[0])
        
        for i in result:
            if puzzle[(abs(i) - 1) // m][(abs(i) - 1) % m] == "_":
                newPuzzle[(abs(i) - 1) // m][(abs(i) - 1) % m] = "T" if i > 0 else "G"
                
        for i in range(n):
            for j in range(m):
                if newPuzzle[i][j] == "_":
                    newPuzzle[i][j] = "G"
                    
    return check, newPuzzle
