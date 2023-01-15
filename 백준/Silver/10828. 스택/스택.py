import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    inp = sys.stdin.readline().split()
    cmd = inp[0]

    if cmd == 'push':
        stack.append(int(inp[1]))
    if cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if cmd == 'size':
        print(len(stack))
    if cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)