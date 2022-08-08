T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    numbers = []
    cnt = 0
    for i in range(N, M + 1):
        numbers.append(i)
    for j in numbers:
        list_ = list(str(j))
        cnt += int(list_.count('0'))
    print(cnt)
