T = int(input())

for i in range(1, T + 1):
    N = int(input())
    earn = list(map(int, input().split()))
    aver = sum(earn) / N
    cnt = 0
    for j in earn:
        if j <= aver:
            cnt += 1
    print(f'#{i} {cnt}')