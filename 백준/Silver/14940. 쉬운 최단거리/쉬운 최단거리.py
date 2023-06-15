from collections import deque

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
start = deque()
distance = [[-1] * m for _ in range(n)]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            start.append((i, j))
            distance[i][j] = 0
            break

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]  # 방향 탐색 리스트

while start:  # start가 빌 때 까지
    x, y = start.popleft()
    for i in range(4):  # 네방향 탐색
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and distance[nx][ny] == -1:  # 갈수있는 길이고 거리가 -1 이라면
                distance[nx][ny] = distance[x][y] + 1
                start.append((nx, ny))  # 이동한 좌표값 start에 넣기

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(0, end=" ")
        elif matrix[i][j] == 2:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()
