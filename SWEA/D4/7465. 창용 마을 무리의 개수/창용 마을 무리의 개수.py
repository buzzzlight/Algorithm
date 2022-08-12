T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split()) # 사람 수, 관계 수
    people = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    cnt = 0

    for j in range(M):
        u, v = map(int, input().split())
        people[u].append(v)
        people[v].append(u)

    for k in range(1, N + 1):
        if visited[k] == 0:
            stack = [k]
            visited[k] = 1
            while stack:
                cur = stack.pop()
                for adj in people[cur]:
                    if visited[adj] == 0:
                        stack.append(adj)
                        visited[adj] = 1
            cnt += 1

    print(f'#{i} {cnt}')