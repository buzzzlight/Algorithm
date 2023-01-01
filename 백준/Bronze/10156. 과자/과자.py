K, N, M = map(int, input().split())
money = M - K * N

if money >= 0:
    print(0)
else:
    print(-money)