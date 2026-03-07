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

def zonerowswap(matrix):
    block = int(input()) - 1

    row1 = block * 3
    row2 = row1 + 3

    for i in range(3):
        matrix[row1 + i], matrix[row2 + i] = matrix[row2 + i], matrix[row1 + i]

    return matrix

for row in table:
    print(row)

print('===========================')
newtable = zonerowswap(table)

for row in newtable:
    print(row)


