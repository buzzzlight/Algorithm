from collections import deque

N, M, V = map(int, input().split())
graph = []

for _ in range(N + 1):
    graph.append([0] * (N + 1))

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visited = [0] * (N + 1)
visited2 = [0] * (N + 1)

def dfs(V):
    visited2[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):
        if visited2[i] == 0 and graph[V][i] == 1:
            dfs(i)

def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if visited[i] == 0 and graph[V][i] == 1:
                q.append(i)
                visited[i] = 1

dfs(V)
print()
bfs(V)