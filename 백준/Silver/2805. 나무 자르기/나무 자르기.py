n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in tree:
        if i >= mid:
            sum += (i - mid)
    
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)