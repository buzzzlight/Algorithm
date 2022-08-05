N = int(input())
numbers = list(map(int, input().split()))
min_ = numbers[0]
max_ = numbers[0]

for i in range(N):
    if numbers[i] < min_:
        min_ = numbers[i]

for i in range(N):
    if numbers[i] > max_:
        max_ = numbers[i]

print(min_, max_)