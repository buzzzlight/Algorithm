N = int(input())
cow = []
for _ in range(11):
    cow.append([])
for i in range(N):
    u, v = map(int, input().split())
    cow[u].append(v)

cnt = 0

for i in range(11):
    if len(cow[i]) >= 2:
        for j in range(len(cow[i]) - 1):
            if cow[i][j] != cow[i][j + 1]:
                cnt += 1

print(cnt)