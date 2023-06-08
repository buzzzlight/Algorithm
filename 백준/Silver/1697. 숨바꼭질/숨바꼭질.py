from collections import deque

n, k = map(int, input().split())
time = 0

queue = deque([(n, 0)])  # (위치, 시간)
visited = set([n])  # 방문한 위치 저장

while queue:
    p, time = queue.popleft()

    if p == k:
        print(time)

    p2 = [p * 2, p + 1, p - 1]

    for i in p2:
        if i >= 0 and i <= 100000 and i not in visited:
            queue.append((i, time + 1))
            visited.add(i)
