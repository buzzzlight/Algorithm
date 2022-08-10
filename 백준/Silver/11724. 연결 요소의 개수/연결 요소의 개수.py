N, M = map(int, input().split())

graph = []
for _ in range(N + 1):
    graph.append([])

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []
for _ in range(N + 1):
    visited.append(0)

cnt = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        stack = [i]
        visited[i] = 1
        while stack:
            cur = stack.pop()
            for adj in graph[cur]:
                if visited[adj] == 0:
                    stack.append(adj)
                    visited[adj] = 1
        cnt += 1

print(cnt)