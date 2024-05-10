import os

#Tổng hệ số của các ô trong vùng lân cận của ô [row][col]
def sum_adjacent_coefficient(board, row, col, rows, cols): 
    sum = 0
    for row_relative_pos in [-1, 0, 1]:
        for col_relative_pos in [-1, 0, 1]:
            if row_relative_pos == 0 and col_relative_pos == 0: 
                continue
            row_absolute_pos = row + row_relative_pos
            col_absolute_pos = col + col_relative_pos

            if 0 <= row_absolute_pos < rows and 0 <= col_absolute_pos < cols and board[row_absolute_pos][col_absolute_pos].isdigit():
                if board[row_absolute_pos][col_absolute_pos] == '0':
                    return 0
                else:
                    sum += int(board[row_absolute_pos][col_absolute_pos])
    return sum

#Giảm hệ số của các ô trong vùng lân cận của ô [row][col]
def decrement_adjacent_coefficient(board, row, col, rows, cols):  
    for row_relative_pos in [-1, 0, 1]:
        for col_relative_pos in [-1, 0, 1]:
            if row_relative_pos == 0 and col_relative_pos == 0: 
                continue
            row_absolute_pos = row + row_relative_pos
            col_absolute_pos = col + col_relative_pos
            if 0 <= row_absolute_pos < rows and 0 <= col_absolute_pos < cols and board[row_absolute_pos][col_absolute_pos].isdigit() and int(board[row_absolute_pos][col_absolute_pos]) > 0:
                board[row_absolute_pos][col_absolute_pos] = str(int(board[row_absolute_pos][col_absolute_pos]) - 1)

def brute_force(board,rows,cols):
    result =[]
    for row in range(rows):
        row_result =[]
        for col in range(cols):
            row_result.append(board[row][col])
        result.append(row_result)

    if rows is None:
        return

    while True:
        max_count = 0 

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '_':
                    count = sum_adjacent_coefficient(board, row, col, rows, cols)
                    if count > max_count:
                        max_count = count
                        max_row = row
                        max_col = col

        if max_count == 0:
            break
        
        board[max_row][max_col] = 'T'
        decrement_adjacent_coefficient(board, max_row, max_col, rows, cols) 
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == '_':
                board[row][col] = 'G'

    for row in range(rows):
        for col in range(cols):
            if result[row][col] == '_':
                result[row][col] = board[row][col]

    check = check_traps(result, rows, cols)

    for row in range(rows):
        for col in range(cols):
            if col != cols-1:
                result[row][col]= result[row][col]+','
    if not check:
        return check,None
    
    return check, result

#Đếm số trap xung quanh ô [row][cow]
def count_traps(result, row, col, rows, cols): 
    count = 0
    for row_relative_pos in [-1, 0, 1]:
        for col_relative_pos in [-1, 0, 1]:
            if row_relative_pos == 0 and col_relative_pos == 0: 
                continue
            row_absolute_pos = row + row_relative_pos
            col_absolute_pos = col + col_relative_pos

            if 0 <= row_absolute_pos < rows and 0 <= col_absolute_pos < cols and result[row_absolute_pos][col_absolute_pos] == 'T':
                count += 1
    return count

# Kiểm tra số lượng trap có đúng với số biểu diễn ở ô [row][col]
def check_traps(result, rows, cols): 
    check = True
    flag = True
    for row in range(rows):
        for col in range(cols):
            if result[row][col].isdigit() and count_traps(result, row, col, rows, cols) != int(result[row][col]) :
                check = False
                flag = False
                break
            
        if not flag:
            break    
    return check    