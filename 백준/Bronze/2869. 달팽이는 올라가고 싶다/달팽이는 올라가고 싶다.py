import math
a, b, v = map(int, input().split())
cnt = (v - a) / (a - b)

if cnt + 1 == int(cnt + 1):
    print(int(cnt + 1))
else:
    print(int(math.ceil(cnt + 1)))