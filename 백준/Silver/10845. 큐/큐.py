import sys
from collections import deque

q = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    inp = sys.stdin.readline().split()
    cmd = inp[0]

    if cmd == 'push':
        q.append(inp[1])
    elif cmd == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)