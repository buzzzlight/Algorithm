k, n = map(int, input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)