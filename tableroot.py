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

for row in table:
    print(row)
a = input()
