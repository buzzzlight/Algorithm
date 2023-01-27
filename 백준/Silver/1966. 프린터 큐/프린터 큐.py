T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    imprt = list(map(int, input().split()))
    idx = list(range(len(imprt)))
    idx[M] = 'target'
    order = 0

    while True:
        if imprt[0] == max(imprt):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                imprt.pop(0)
                idx.pop(0)
        else:
            imprt.append(imprt.pop(0))
            idx.append(idx.pop(0))