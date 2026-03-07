size = 9
table = []

digit = [1, 4, 7, 2, 5, 8, 3, 6, 9]

for i in range(size):
    row = []
    start = digit[i]
    for j in range(size):
        num = ((start - 1 + j) % 9) + 1
        row.append(num)
    table.append(row)

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] 
            for i in range(len(matrix[0]))]

for row in table:
    print(row)

print('===========================')
transposed_table = transpose(table)

for row in transposed_table:
    print(row)
