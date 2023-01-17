n = int(input())
seq = []
answer = []
a = 1
flag = False

for _ in range(n):
    x = int(input())
    while a <= x:
        seq.append(a)
        answer.append('+')
        a += 1
    if seq[-1] == x:
        seq.pop()
        answer.append('-')
    else:
        flag = True
        print('NO')
        break

if flag == False:
    for i in answer:
        print(i)