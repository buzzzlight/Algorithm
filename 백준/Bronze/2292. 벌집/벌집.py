n = int(input())
cnt = 1
bee = 1

if n == 1:
    print(1)
else:
    while True:
        bee += cnt * 6
        cnt += 1
        if bee >= n:
            break
    print(cnt)