n, m = map(int, input().split())
ball = []

for a in range(1, n + 1):
    ball.append(a)

for b in range(m):
    i, j = map(int, input().split())
    temp = ball[i - 1]
    ball[i - 1] = ball[j - 1]
    ball[j - 1] = temp

for c in ball:
    print(c, end=" ")