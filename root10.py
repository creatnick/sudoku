import random
import tkinter as tk
import time
import winsound

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

def show_board(puzzle, solution):
    game_active = True
    start_time = time.time()
    hints_left = 3
    errors = 0
    
    root = tk.Toplevel()
    root.title("Судоку")
    center_window(root, 315, 381)

    hints_left = 3
    cells = [[None for _ in range(9)] for _ in range(9)]
    

    def validate(P):
        return P == "" or (len(P) == 1 and P in "123456789")

    vcmd = (root.register(validate), '%P')

    def check_cell(event, row, col):
        nonlocal errors

        val = cells[row][col].get()

        if val == "":
            cells[row][col].config(bg="white")
            return

        if int(val) != solution[row][col]:
            cells[row][col].config(bg="red")
            if sound_enabled:
                winsound.PlaySound("sounds\\wrong.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

            errors += 1
            error_label.config(text=f'Ошибки: {errors}/{max_errors}')

            if errors >= max_errors:
                game_over()

        else:
            cells[row][col].config(bg='green')
            if sound_enabled:
                winsound.PlaySound("sounds\\correct.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

            if check_win():
                win_game()
            
            

    def give_hint():
        nonlocal hints_left

        if hints_left <= 0:
            return

        available_cells = []

        for i in range(9):
            for j in range(9):

                current = cells[i][j].get()

                if current == "":
                    available_cells.append((i, j))

                elif int(current) != solution[i][j]:
                    available_cells.append((i, j))

        if not available_cells:
            return

        row, col = random.choice(available_cells)

        cells[row][col].config(state="normal")

        cells[row][col].delete(0, tk.END)
        cells[row][col].insert(0, str(solution[row][col]))

        cells[row][col].config(
            state="readonly",
            readonlybackground="green"
        )

        hints_left -= 1

        hint_button.config(text=f"Подсказка: {hints_left}/3")

        if hints_left == 0:
            hint_button.config(state="disabled")

        if check_win():
            win_game()

    time_label = tk.Label(root, text="00:00:00", font=("Arial", 12))
    time_label.grid(row=0, column=0, columnspan=3, pady=10)

    hint_button = tk.Button(root, text=f"Подсказка: {hints_left}/3", command=give_hint)
    hint_button.grid(row=0, column=0, columnspan=9, pady=10)
    error_label = tk.Label(root, text=f"Ошибки: {errors}/{max_errors}", font=("Arial", 12))
    error_label.grid(row=0, column=6, columnspan=4, pady=10)
    if hints_left == 0:
        hint_button.config(state="disabled")

    for i in range(9):
        for j in range(9):
            val = puzzle[i][j]

            e = tk.Entry(root,width=2,font=("Arial", 20),justify="center",validate="key",validatecommand=vcmd)
            padx = (0, 0)
            pady = (0, 0)

            if j in (2, 5):
                padx = (0, 5)
            if i in (2, 5):
                pady = (0, 5)

            e.grid(row=i+2, column=j, padx=padx, pady=pady)

            if val != 0:
                e.insert(0, str(val))
                e.config(state="readonly", readonlybackground="white")
            else:
                e.bind("<KeyRelease>", lambda event, r=i, c=j: check_cell(event, r, c))

            cells[i][j] = e
    def game_over():
        popup = tk.Toplevel(root)
        popup.title("Проигрыш")
        center_window(popup, 200, 100)

        tk.Label(popup, text="вы проиграли", font=("Arial", 14)).pack(padx=20, pady=10)
        tk.Button(popup, text="Закрыть", command=root.destroy).pack(pady=10)
        nonlocal game_active
        game_active = False

    def win_game():
        nonlocal game_active
        game_active = False

        popup = tk.Toplevel(root)
        popup.title("Победа")
        center_window(popup, 250, 120)

        tk.Label(popup, text="Вы победили!", font=("Arial", 16) ).pack(pady=15)

        tk.Button(popup, text="Закрыть", command=root.destroy).pack(pady=10)

    def check_win():
        for i in range(9):
            for j in range(9):
                val = cells[i][j].get()

                if val == "":
                    return False

                if int(val) != solution[i][j]:
                    return False

        return True
        
    def update_timer():
        if not game_active:
            return

        elapsed = int(time.time() - start_time)

        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60

        time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        root.after(1000, update_timer)

    update_timer()


def start_game():
    seed = []
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

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Настройки")
    settings_window.resizable(False, False)
    center_window(settings_window, 600, 400)

    title = tk.Label(settings_window, text="Настройки", font=("Arial", 24))
    title.place(x=220, y=20)

    errors_label = tk.Label(settings_window,text="Количество ошибок",font=("Arial", 18))
    errors_label.place(x=50, y=100)

    def toggle_sound():
        current = sound_var.get()
        sound_var.set(not current)
        if sound_var.get():
            sound_button.config(text="ВКЛ")
        else:
            sound_button.config(text="ВЫКЛ")

    def save():
        global max_errors
        global sound_enabled

        try:
            max_errors = int(error_entry.get())
        except:
            pass
        sound_enabled = sound_var.get()
        settings_window.destroy()



    error_entry = tk.Entry(settings_window, font=("Arial", 18), justify="center", width = 10)
    error_entry.insert(0, str(max_errors))
    error_entry.place(x=350, y=100)

    sound_label = tk.Label(settings_window, text="Звуковые эффекты", font=("Arial", 18))
    sound_label.place(x=50, y=180)

    sound_var = tk.BooleanVar(value=sound_enabled)
    sound_button = tk.Button(settings_window, text="ВКЛ"
                             if sound_enabled
                             else "ВЫКЛ", font=(("Arial"), 18),width=8)
    

    sound_button.config(command=toggle_sound)
    sound_button.place(x=350, y=175)

    menu_button = tk.Button(settings_window, text="Главное меню", font=("Arial", 18), width=15, command=save)
    menu_button.place(x=180, y=320)

def open_rules():
    rules_window = tk.Toplevel(root)
    rules_window.title("Правила")
    center_window(rules_window,750, 450)
    rules_window.resizable(False, False)
    title = tk.Label(rules_window,text="Правила",font=("Arial", 24, "bold"))
    title.place(x=280, y=15)
    img = tk.PhotoImage(file="rules.png")
    image_label = tk.Label(rules_window, image=img)
    image_label.image = img
    image_label.place(x=400, y=70)
    
    tk.Button(rules_window,text="Главное меню",font=("Arial", 14),command=rules_window.destroy).place(x=280, y=380)
    
    rules_text = ("Игровое поле представляет собой квадрат \n"
                  "размером 9х9, разделённый на меньшие квадраты\n"
                  "со сторонами в 3 клетки. В некоторых в начале игры\n"
                  "уже стоят некоторые числа (от 1 до 9)\n\n"
                  "Игрок должен заполнить пустые клетки\n"
                  "цифрами от 1 до 9 так, чтобы числа не повторялись:\n"
                  "- в каждой строке\n"
                  "- в каждом столбце\n"
                  "- в каждом квадрате 3×3")

    text_label = tk.Label(rules_window,text=rules_text,justify="left",font=("Arial", 12))
    text_label.place(x=20, y=60)

def center_window(window, width, height):
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    x = (screen_w - width) // 2
    y = (screen_h - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

n = 18
seed = []
num = [1, 4, 7]
max_errors = 3
sound_enabled = True
act = ['tr', 'sr', 'sc', 'ar', 'ac']
root = tk.Tk()

screen_w = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_w - 300) // 2
y = (screen_height - 200) // 2

root.title("Судоку")
center_window(root, 600, 380)
root.resizable(False, False)
title = tk.Label(root, text="Судоку", font=("Arial", 64, "bold"))
title.place(x=150, y=40)

tk.Button(root, text="Начать игру", font=("Arial", 18), command=start_game).place(x=226, y=200)
tk.Button(root, text="Настройки", font=("Arial", 18),command=open_settings).place(x=230, y=260)
tk.Button(root, text="Правила", font=("Arial", 18), command=open_rules).place(x=240, y=320)





root.mainloop()
