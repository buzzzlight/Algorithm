N = int(input())
cnt = 0

for i in range(1, N + 1):
    if i < 100:
        cnt += 1
    else:
        hansu = list(map(int, str(i)))
        if hansu[0] - hansu[1] == hansu[1] - hansu[2]:
            cnt += 1

print(cnt)