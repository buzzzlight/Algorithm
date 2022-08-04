N, M = map(int, input().split())
bread = []
for i in range(N):
    bread.append(list(input()))

fall = []
for i in range(N):
    fall.append([0] * M)

for i in range(N):
    for j in range(M):
        fall[i][j] = bread[i][(M - 1) - j]
        print(fall[i][j], end='')
    print()
