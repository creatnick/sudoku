import random
diff = int(input()) * 5
seed = []
num = [1, 4, 7]
act = ['tr', 'sr', 'sc', 'ar', 'ac']
for i in range (diff):
    temp = random.choice(act)
    if temp == 'tr':
        seed.append('t')
    if temp == 'sr':
        seed.append('sr')
        x = random.choice(num)
        seed.append(str(x))
        seed.append(str(x+2))
    if temp == 'sc':
        seed.append('sc')
        x = random.choice(num)
        seed.append(str(x))
        seed.append(str(x+2))
    if temp == 'ar':
        seed.append('ar')
        x = random.randint(2, 3)
        seed.append(str(x))
        seed.append(str(x-1))
    if temp == 'ac':
        seed.append('ac')
        x = random.randint(2, 3)
        seed.append(str(x))
        seed.append(str(x-1))
    
    


print(''.join(seed))
