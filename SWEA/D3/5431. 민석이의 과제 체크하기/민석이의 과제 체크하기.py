T = int(input())

for _ in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    fail = []
    for i in range(1, N + 1):
        if i not in numbers:
            fail.append(i)
    fail = ' '.join(map(str, fail))
    print(f'#{_} {str(fail)}')