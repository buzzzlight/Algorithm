word = input()
number = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5,
            'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
time = 0

for i in word:
    for j in number.keys():
        if str(i) in j:
            time += number.get(j) + 1

print(time)
