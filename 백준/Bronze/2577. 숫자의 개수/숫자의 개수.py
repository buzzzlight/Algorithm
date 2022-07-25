A = int(input())
B = int(input())
C = int(input())

multiple = str(A * B * C)

for i in range(10):
    cnt = 0
    for j in multiple:
        if str(i) == j:
            cnt += 1
    print(cnt)