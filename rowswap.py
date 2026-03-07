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

def rowswap(matrix):
    row1 = int(input()) - 1 
    if row1 % 3 != 0:
        return matrix
    
    row2 = row1 + 2
    
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    
    return matrix

for row in table:
    print(row)

print('===========================')
newtable = rowswap(table)

for row in newtable:
    print(row)
