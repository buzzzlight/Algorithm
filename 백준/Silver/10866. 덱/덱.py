import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque([])

for i in range(N):
    inp = sys.stdin.readline().split()
    cmd = inp[0]

    if cmd == 'push_front':
        deq.appendleft(int(inp[1]))
    elif cmd == 'push_back':
        deq.append(int(inp[1]))
    elif cmd == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(deq))
    elif cmd == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)