import random
import tkinter as tk

def colswap(matrix, col):
    col -= 1
    col2 = col + 2
    for i in range(len(matrix)):
        matrix[i][col], matrix[i][col2] = matrix[i][col2], matrix[i][col]
    return matrix

def rowswap(matrix, row):
    row -= 1
    row2 = row + 2
    matrix[row], matrix[row2] = matrix[row2], matrix[row]
    return matrix

def zonerowswap(matrix, zone):
    zone -= 1
    row1 = zone * 3
    row2 = row1 + 3
    for i in range(3):
        matrix[row1 + i], matrix[row2 + i] = matrix[row2 + i], matrix[row1 + i]
    return matrix

def zonecolswap(matrix, zone):
    zone -= 1
    col1 = zone * 3
    col2 = col1 + 3
    for row in range(len(matrix)):
        for i in range(3):
            matrix[row][col1 + i], matrix[row][col2 + i] = matrix[row][col2 + i], matrix[row][col1 + i]
    return matrix

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = row - row % 3, col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def count_solutions(board):
    count = 0

    def solve_count(b):
        nonlocal count
        if count > 1:
            return

        for row in range(9):
            for col in range(9):
                if b[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(b, row, col, num):
                            b[row][col] = num
                            solve_count(b)
                            b[row][col] = 0
                    return
        count += 1

    solve_count([row[:] for row in board])
    return count


def remove_cells_smart(board, attempts=40):
    puzzle = [row[:] for row in board]

    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if puzzle[row][col] == 0:
            continue

        backup = puzzle[row][col]
        puzzle[row][col] = 0

        copy_board = [r[:] for r in puzzle]
        solutions = count_solutions(copy_board)

        if solutions != 1:
            puzzle[row][col] = backup

        attempts -= 1

    return puzzle

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print('-' * 21)

        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')

            if val == 0:
                print('_', end=' ')
            else:
                print(val, end=' ')
        print()

import tkinter as tk

def show_board(puzzle, solution):
    root = tk.Tk()
    root.title("Судоку")

    cells = [[None for _ in range(9)] for _ in range(9)]

    def validate(P):
        return P == "" or (len(P) == 1 and P in "123456789")

    vcmd = (root.register(validate), '%P')

    def check_cell(event, row, col):
        val = cells[row][col].get()

        if val == "":
            cells[row][col].config(bg="white")
            return

        if int(val) != solution[row][col]:
            cells[row][col].config(bg="red")

    for i in range(9):
        for j in range(9):
            val = puzzle[i][j]

            e = tk.Entry(
                root,
                width=2,
                font=("Arial", 20),
                justify="center",
                validate="key",
                validatecommand=vcmd
            )

            # отступы для блоков 3x3
            padx = (0, 0)
            pady = (0, 0)

            if j in (2, 5):
                padx = (0, 5)
            if i in (2, 5):
                pady = (0, 5)

            e.grid(row=i, column=j, padx=padx, pady=pady)

            if val != 0:
                e.insert(0, str(val))
                e.config(state="readonly", readonlybackground="#dddddd")
            else:
                e.bind("<KeyRelease>", lambda event, r=i, c=j: check_cell(event, r, c))

            cells[i][j] = e

    root.mainloop()


n = 18
seed = []
num = [1, 4, 7]
act = ['tr', 'sr', 'sc', 'ar', 'ac']


while True:
    for _ in range(n):
        temp = random.choice(act)
        if temp == 'tr':
            seed.append('t')
        elif temp == 'sr':
            seed.append('sr')
            x = random.choice(num)
            seed.append(str(x))
            seed.append(str(x + 2))
        elif temp == 'sc':
            seed.append('sc')
            x = random.choice(num)
            seed.append(str(x))
            seed.append(str(x + 2))
        elif temp == 'ar':
            seed.append('ar')
            x = random.randint(2, 3)
            seed.append(str(x))
            seed.append(str(x - 1))
        elif temp == 'ac':
            seed.append('ac')
            x = random.randint(2, 3)
            seed.append(str(x))
            seed.append(str(x - 1))

    key = ''.join(seed)

    size = 9
    digit = [1, 4, 7, 2, 5, 8, 3, 6, 9]
    table = []
    for i in range(size):
        row = []
        start = digit[i]
        for j in range(size):
            num_val = ((start - 1 + j) % 9) + 1
            row.append(num_val)
        table.append(row)

    i = 0
    while i < len(key):
        if key[i] == 't':
            table = transpose(table)
            i += 1
        elif key[i] == 's':
            if i + 1 >= len(key):
                break
            cmd = key[i:i+2]
            if cmd == 'sr':
                if i + 3 < len(key):
                    x = int(key[i+2])
                    table = rowswap(table, x)
                    i += 4
                else:
                    break
            elif cmd == 'sc':
                if i + 3 < len(key):
                    x = int(key[i+2])
                    table = colswap(table, x)
                    i += 4
                else:
                    break
            else:
                i += 1
        elif key[i] == 'a':
            if i + 1 >= len(key):
                break
            cmd = key[i:i+2]
            if cmd == 'ar':
                if i + 3 < len(key):
                    x = int(key[i+2])
                    table = zonerowswap(table, x - 1)
                    i += 4
                else:
                    break
            elif cmd == 'ac':
                if i + 3 < len(key):
                    x = int(key[i+2])
                    table = zonecolswap(table, x - 1)
                    i += 4
                else:
                    break
            else:
                i += 1
        else:
            i += 1

    puzzle = remove_cells_smart(table, 45)

    show_board(puzzle, table)
