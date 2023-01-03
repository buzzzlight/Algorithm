import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M):
    temp = sys.stdin.readline().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif temp[0] == 'empty':
            S = set()

    else:
        cal, x = temp[0], int(temp[1])

        if cal == 'add':
            S.add(x)
        elif cal == 'remove':
            S.discard(x)
        elif cal == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cal == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)