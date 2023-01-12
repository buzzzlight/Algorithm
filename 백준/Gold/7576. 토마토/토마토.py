from collections import deque
M, N = map(int, input().split())

matrix = []
start = deque()

for i in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)
    for j in range(M):
        if arr[j] == 1:
            start.append((i, j))

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

while start:
    x, y = start.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                start.append((nx, ny))

flag = False
max_num = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            flag = True
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]

if flag == False:
    print(max_num-1)
else:
    print(-1)