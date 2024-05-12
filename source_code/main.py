import os
import time
import signal
import sys
from brute_force import* 
from solveCNF_without_library import *
from solve_by_pysat import *
from back_tracking import *

# ---------Hàm xử lý khi chương trình bị ngắt----------
def handler(signum, frame):
    print("Đã quá thời gian quy định là 3 phút chạy chương trình nên chương trình tự động ngắt.")
    sys.exit(1)

signal.signal(signal.SIGALRM, handler)

# Đặt hẹn giờ cho 3 phút=180s
signal.alarm(180)  
#---------------------------------------
def main():
    path_input_folder = 'testcases/input'
    path_output_folder = 'testcases/output'

    path_input_files = []
    path_output_files = []

    for i in range(num_of_file(path_input_folder)):
        path_input_files.append(f"{path_input_folder}/input{i}.txt")
        path_output_files.append(f"{path_output_folder}/output{i}.txt")
    print("--------MENU----------------")
    print("1.Giải CNF sử dụng thư viện")
    print("2.Giải CNF mà không sử dụng thư viện")
    print("3.Sử dụng thuật toán Brute-force")
    print("4.Sử dụng thuật toán Backtracking")
    choose = int(input("Lựa chọn thuật toán mà bạn muốn làm: "))
    while choose <1 or choose >4:
        choose = int(input("Chọn sai, mời chọn lại: "))
    
    for i in range(num_of_file(path_input_folder)):
        start = time.time()

        write_output_file(path_input_files[i], path_output_files[i],choose)

        end = time.time()

        # Tính thời gian chạy
        running_time = end - start
        print(f"-Thời gian chạy file input{i}.txt là: {running_time: 4f} giây")


def num_of_file(path_folder):
    count = 0
    files = os.listdir(path_folder)

    for file in files:
        path_file = os.path.join(path_folder, file)
        if os.path.isfile(path_file):
            count += 1

    return count

def read_input_file(path_input_file):
    try:
        with open(path_input_file, 'r') as f:
            lines = f.readlines()
            puzzle = []
            for line in lines:
                line = line.rstrip('\n')
                row = []
                for cell in line.split(', '):
                    row.append(cell)
                puzzle.append(row)
            return puzzle
    except Exception as e:
        print(f"Không thể đọc file: {str(e)}")
        return None, None, None

def write_output_file(path_input_file,path_output_file,choose):
    puzzle = read_input_file(path_input_file)
    if choose==1:
        #Solve CNF by pysat
        check, result = solve_by_pysat(puzzle)
    elif choose==2:
        #Solve CNF without library
        check,result=doDPLL(puzzle)
    elif choose==3:
        #Brute-force algorithm
        rows = len(puzzle)
        cols = len(puzzle[0])
        check, result = brute_force(puzzle,rows,cols)
    elif choose==4:
        check, result = solve_with_backtracking(puzzle)
        

    with open(path_output_file, 'w') as f:
        if check:
            for row in result:
                row_str = ' '.join(map(str, row))  
                f.write(row_str + '\n') 
        else:
            f.write('FALSE' + '\n')



if __name__ == "__main__":
    main()
