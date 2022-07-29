T = int(input())

for i in range(1, T + 1):
    rec = list(map(int,input().split()))
    for j in rec:
        if rec.count(j) == 1:
            print(f'#{i} {j}')
        if rec.count(j) == 3:
            print(f'#{i} {j}')
            break