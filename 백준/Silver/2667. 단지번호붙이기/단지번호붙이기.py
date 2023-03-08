from collections import deque

n = int(input())
graph = []
cnt = []

for _ in range(n):
    graph.append(list(map(int, input())))   # 행렬 만들기

def bfs(x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]   # 방향 탐색 리스트

    queue = deque()
    queue.append((x, y)) # 시작점 추가
    graph[x][y] = 0  # 방문처리
    count = 1

    while queue:    # queue가 빌 때 까지 반복
        x, y = queue.popleft()
        for i in range(4):  # 네방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문처리
                queue.append((nx, ny))
                count += 1

    cnt.append(count)
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)