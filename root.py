size = 9
table = []
temprow = []

digit = [1, 4, 7, 2, 5, 8, 3, 6, 9]

def colswap(matrix):
    col = int(input('введите номер столбца (1, 4, 7): ')) - 1    
    col2 = col + 2
    
    for i in range(len(matrix)):
        matrix[i][col], matrix[i][col2] = matrix[i][col2], matrix[i][col]
    
    return matrix
    for row in table:
        print(row)
        print('===========================')

def rowswap(matrix):
    row1 = int(input('введите номер строки (1, 4, 7):  ')) - 1 
    if row1 % 3 != 0:
        return matrix
    
    row2 = row1 + 2
    
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    
    return matrix
    for row in table:
        print(row)
        print('===========================')

def zonerowswap(matrix):
    block = int(input('введите номер района: ')) - 1

    row1 = block * 3
    row2 = row1 + 3

    for i in range(3):
        matrix[row1 + i], matrix[row2 + i] = matrix[row2 + i], matrix[row1 + i]

    return matrix

def zonecolswap(matrix):
    zone = int(input('введите номер района: ')) - 1

    col1 = zone * 3
    col2 = col1 + 3

    for row in range(len(matrix)):
        for i in range(3):
            matrix[row][col1 + i], matrix[row][col2 + i] = matrix[row][col2 + i], matrix[row][col1 + i]

    return matrix

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] 
            for i in range(len(matrix[0]))]

for i in range(size):
    row = []
    start = digit[i]
    for j in range(size):
        num = ((start - 1 + j) % 9) + 1
        row.append(num)
    table.append(row)



while True:
    print('===========================')

    for row in table:
        print(row)
        
    print('===========================')
    print('1 - смена столбцов')
    print('2 - смена смена строк')
    print('3 - смена горизонтальных районов')
    print('4 - смена вертикальных районов')
    print('5 - транспортировка таблицы')
    mode = int(input('введите номер действия: '))
    if mode == 1:
        colswap(table)
    if mode == 2:
        rowswap(table)
    if mode == 3:
        zonerowswap(table)
    if mode == 4:
        zonecolswap(table)
    if mode == 5:
        table = transpose(table)
