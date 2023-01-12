from collections import deque

N, M = map(int, input().split())

matrix = []
for i in range(N):
    arr = list(map(int, input()))
    matrix.append(arr)

visited = []
for i in range(N):
    arr = [0] * M
    visited.append(arr)

start = deque()
start.append((0, 0))
visited[0][0] = 1

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

while start:
    x, y = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                start.append((nx, ny))
