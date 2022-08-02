N = int(input())
numbers = []

for i in range(N):
    n = int(input())
    numbers.append(n)

for i in sorted(numbers):
    print(i)