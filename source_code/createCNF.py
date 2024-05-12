import itertools

def createCNFs(puzzle):
    m = len(puzzle[0])
    clauses = []
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != "_":
                clauses += pointCNF(puzzle, i, j)

    #unique_clauses = set(tuple(sublist) for sublist in clauses)
    #clauses = [list(item) for item in unique_clauses]
    return clauses

def pointCNF(p, r, c): #puzzle, row, column are considered
    n = len(p) #number of rows
    m = len(p[r]) #number of columns
    atomic = []
    for i in range(max(0, r - 1), min(r + 2, n)):
        for j in range(max(0, c - 1), min(c + 2, m)):
            if p[i][j] == "_":
               atomic.append(m*i + j + 1) #add index of p[i][j] in row-major order

    cnf = []
    n = len(atomic)

    if p[r][c] == n:
        cnf = [[i] for i in atomic]
    elif p[r][c] == 0:
        cnf = [[-i] for i in atomic]
    else:
        for i in range(n + 1):
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
