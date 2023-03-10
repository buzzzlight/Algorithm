n, m = map(int, input().split())
basket = []

for a in range(1, n + 1):
    basket.append(a)

for _ in range(m):
    i, j = map(int, input().split())
    basket = basket[:i-1] + basket[i-1:j][::-1] + basket[j:]

for k in basket:
    print(k, end=' ')