F = []
for _ in range(8):
    F.append(list(input()))

cnt = 0
for i in range(8):
    for j in range(8):
        if F[i][j] == 'F':
            if (i + j) % 2 == 0:
                cnt += 1

print(cnt)