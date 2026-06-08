import random

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

    print('===========================')
    for row in table:
        print(row)
    print('===========================')
    input()
