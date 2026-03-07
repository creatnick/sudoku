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

def colswap(matrix):
    col = int(input()) - 1    
    col2 = col + 2
    
    for i in range(len(matrix)):
        matrix[i][col], matrix[i][col2] = matrix[i][col2], matrix[i][col]
    
    return matrix

for row in table:
    print(row)

print('===========================')
newtable = colswap(table)

for row in newtable:
    print(row)
