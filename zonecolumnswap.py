size = 9
table = []
temprow = []

digit = [1, 4, 7, 2, 5, 8, 3, 6, 9]

for i in range(size):
    row = []
    start = digit[i]
    for j in range(size):
        num = ((start - 1 + j) % 9) + 1
        row.append(num)
    table.append(row)

def zonecolswap(matrix):
    zone = int(input()) - 1

    col1 = zone * 3
    col2 = col1 + 3

    for row in range(len(matrix)):
        for i in range(3):
            matrix[row][col1 + i], matrix[row][col2 + i] = matrix[row][col2 + i], matrix[row][col1 + i]

    return matrix

for row in table:
    print(row)

print('===========================')
newtable = zonecolswap(table)

for row in newtable:
    print(row)


