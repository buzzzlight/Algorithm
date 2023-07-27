from collections import deque


def BFS(x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]  # 방향 탐색 리스트
    start.append((x, y))

    while start:  # start가 빌 때 까지
        x, y = start.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and painting[nx][ny] == painting[x][y]
                and not visited[nx][ny]
            ):
                visited[nx][ny] = 1
                start.append((nx, ny))


n = int(input())
painting = [list(input()) for _ in range(n)]
start = deque()

# 적록색약이 아닌 경우
visited = [[0] * n for _ in range(n)]
cnt1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt1 += 1

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if painting[i][j] == "G":
            painting[i][j] = "R"

visited = [[0] * n for _ in range(n)]
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt2 += 1

print(cnt1, cnt2)
