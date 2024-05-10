import os
from createCNF import *
from itertools import product

def read_CNF(puzzle):
    puzzle=list(map(lambda row: [int(i) if i.isdigit() else i for i in row], puzzle))
    cnfs= createCNFs(puzzle)

    return cnfs

def puzzle_1d(puzzle):
    result = []
    for row in puzzle:
        result.extend(row)

    result = ['#'] + result
    return result

def replace_underscore(puzzle_1d):
    indices = [i for i, x in enumerate(puzzle_1d) if x == '_']
    combinations = product(['T', 'G'], repeat=len(indices))
    result = []
    for comb in combinations:
        new_arr = puzzle_1d.copy()
        for i, index in enumerate(indices):
            new_arr[index] = comb[i]
        result.append(new_arr)
    return result

def brute_force(puzzle,row,col):
    result =[]
    check = False
    result_1d =[]

    cnfs = read_CNF(puzzle)
    
    new_puzzle = puzzle_1d(puzzle)
    all_cases = replace_underscore(new_puzzle)
    for item in all_cases:
        new_cnfs = []
        for cnf in cnfs:
            new_cnf = []
            for i in cnf:
                if (i >0):
                    new_cnf.append(item[i])
                else:
                    if item[abs(i)] =='T':
                        new_cnf.append('G')
                    else:
                        new_cnf.append('T')
            new_cnfs.append(new_cnf)
        
        flag = True
        for cnf in new_cnfs:
            if 'T' in cnf:
                continue
            else:
                flag = False
                break
        
    
        if flag:
            check = True
            result_1d = item.copy()
            result_1d.pop(0)
            break

    if not check:
        return check,None
    
    for i in range(row):
        rows = []
        for j in range(col):
            index = i * col + j
            if index < len(result_1d):
                rows.append(result_1d[index])
            else:
                break
        result.append(rows)

    return check,result

