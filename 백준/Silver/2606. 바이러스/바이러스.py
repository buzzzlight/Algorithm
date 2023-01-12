C = int(input())
E = int(input())

graph = []
for _ in range(C + 1):
    graph.append([])
for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []
for _ in range(C + 1):
    visited.append(0)

stack = [1]
visited[1] = 1

while stack:
    cur = stack.pop()
    for adj in graph[cur]:
        if visited[adj] == 0:
            stack.append(adj)
            visited[adj] = 1

print(sum(visited) - 1)
