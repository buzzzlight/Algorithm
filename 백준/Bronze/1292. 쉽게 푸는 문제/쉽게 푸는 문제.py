A, B = map(int, input().split())
number = []

for i in range(1, B + 1):
    for j in range(i):
        number.append(i)

print(sum(number[A-1:B]))