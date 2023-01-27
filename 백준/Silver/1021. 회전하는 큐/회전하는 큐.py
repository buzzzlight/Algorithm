from collections import deque

N, M = map(int, input().split())
loc = list(map(int, input().split()))
idx = deque(list(range(1, N+1)))
answer = 0

for i in loc:
    while True:
        if idx[0] == i:
            idx.popleft()
            break
        else:
            if idx.index(i) < len(idx)/2:
                while idx[0] != i:
                    idx.append(idx.popleft())
                    answer += 1
            else:
                while idx[0] != i:
                    idx.appendleft(idx.pop())
                    answer += 1

print(answer)