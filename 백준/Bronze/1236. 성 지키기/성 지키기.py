N, M = map(int, input().split())
castle = []
n = 0
m = 0

for _ in range(N):
    castle.append(list(input()))

# 컴프리헨션
# castle = [list(input()) for _ in range(N)]

# 행 순회
for i in range(N):
    if 'X' not in castle[i]:
        n += 1

# 열 순회
for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        m += 1

print(max(n, m))