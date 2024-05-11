from createCNF import createCNFs

def solve_with_backtracking(puzzle):
    num_r = len(puzzle)
    num_c = len(puzzle[0])
    clauses = createCNFs(puzzle)
    variables = set(abs(literal) for clause in clauses for literal in clause)
    variables = list(variables)
    assignment = {}

    result = SAT_solver(variables, clauses, assignment)
    if result is None:
        return False, "FALSE"  # When no solution is possible
    
    grid_result = format_solution(result, puzzle, num_r, num_c)
    return True, grid_result

def format_solution(result, puzzle, num_r, num_c):
    grid_result = []
    for i in range(num_r):
        row_result = []
        for j in range(num_c):
            index = i * num_c + j
            if puzzle[i][j] == '_':
                if result.get(index + 1, False):
                    row_result.append('T')  # True means trap
                else:
                    row_result.append('G')  # False means gem
            else:
                row_result.append(puzzle[i][j])
        grid_result.append(row_result)
    return grid_result

def SAT_solver(variables, clauses, assignment):
    if not clauses:
        return assignment  # All clauses satisfied
    
    unassigned = next((v for v in variables if v not in assignment), None)
    if unassigned is None:
        if all_clause_satisfied(clauses, assignment):
            return assignment  # All variables assigned; solution found
        return None

    for value in [True, False]:  # Try both True and False
        assignment[unassigned] = value
        new_clauses = simplify(clauses, unassigned if value else -unassigned)
        result = SAT_solver(variables, new_clauses, assignment)
        if result:
            return result
        assignment.pop(unassigned)  # Backtrack

    return None

def simplify(clauses, literal):
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied
        new_clause = [l for l in clause if -literal != l]
        if not new_clause:
            return []  # Empty clause means unsatisfied; backtrack
        new_clauses.append(new_clause)
    return new_clauses

def all_clause_satisfied(clauses, assignment):
    for clause in clauses:
        if not any((l in assignment and assignment[l] if l > 0 else -l in assignment and not assignment[-l]) for l in clause):
            return False
    return True
