from collections import deque

N, K = map(int, input().split())

queue = deque(list(range(1, N + 1)))
yose = []

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    yose.append(queue.popleft())

print("<", end="")
for i in range(len(yose)-1):
    print(f'{yose[i]}, ', end="")
print(yose[-1], end="")
print(">")