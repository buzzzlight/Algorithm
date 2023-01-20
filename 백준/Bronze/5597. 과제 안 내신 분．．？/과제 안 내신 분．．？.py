numbers = []

for i in range(28):
    numbers.append(int(input()))

for i in range(1, 31):
    if i not in numbers:
        print(i)