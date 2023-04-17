n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

while k != 0:
    for i in coin:
        if (k // i) > 0:
            cnt += (k // i)
            k = k - i * (k // i)

print(cnt)