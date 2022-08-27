n = int(input())

for i in range(1, n + 1):
    i = str(i)
    if '3' in i or '6' in i or '9' in i:
        i = 'X'
        print(i, end=' ')
    else:
        print(i, end=' ')