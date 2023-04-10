arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

x, y = 0, 0
max = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            x = i + 1
            y = j + 1

print(max)
print(x, y)
