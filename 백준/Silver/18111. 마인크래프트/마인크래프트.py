import sys

n, m, b = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr += list(map(int, sys.stdin.readline().split()))

min, max = min(arr), max(arr)
height = 0
ans = 1000000000

for h in range(min, max + 1):
    time = 0
    blocks = b

    for i in arr:
        if i > h: # 높이가 h보다 높으면 블럭 제거
            time += 2 * (i - h)
            blocks += i - h
        else: # 높이가 h보다 낮으면 블럭 추가
            time += h - i
            blocks -= h - i

    if blocks < 0:
        continue
    else:
        if blocks >= 0 and time <= ans:
            ans = time
            height = h

print(ans, height)