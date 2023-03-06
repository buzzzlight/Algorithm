n, m = map(int, input().split())
basket = [0] * n

for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(i, j + 1):
        basket[y - 1] = k

for z in basket:
    print(z, end=' ')