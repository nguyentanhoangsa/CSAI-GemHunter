import os
from brute_force import* 

def main():
    path_input_folder = 'testcases/input'
    path_output_folder = 'testcases/output'

    path_input_files = []
    path_output_files = []

    for i in range(num_of_file(path_input_folder)):
        path_input_files.append(f"{path_input_folder}/input{i}.txt")
        path_output_files.append(f"{path_output_folder}/output{i}.txt")

    for i in range(num_of_file(path_input_folder)):
        write_output_file(path_input_files[i], path_output_files[i])  


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
            board = []
            for line in lines:
                line = line.rstrip('\n')
                row = []
                for cell in line.split(', '):
                    row.append(cell)
                board.append(row)
            return board
    except Exception as e:
        print(f"Không thể đọc file: {str(e)}")
        return None, None, None

def write_output_file(path_input_file,path_output_file):
    board = read_input_file(path_input_file)
    rows = len(board)
    cols = len(board[0])
    #Brute-force algorithm
    check, result = solve_map(board,rows,cols)
    with open(path_output_file, 'w') as f:
        if check:
            for row in result:
                row_str = ' '.join(map(str, row))  
                f.write(row_str + '\n') 
        else:
            f.write('FALSE' + '\n')



if __name__ == "__main__":
    main()