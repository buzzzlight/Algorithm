from collections import deque

t = int(input())

def bfs(x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    graph = [[0] * n for a in range(m)]

    for b in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for c in range(m):
        for d in range(n):
            if graph[c][d] == 1:
                bfs(c, d)
                cnt += 1

    print(cnt)