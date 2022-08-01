K = int(input())
numbers = []

for i in range(K):
    N = int(input())
    if N != 0:
        numbers.append(N)
    else:
        numbers.pop()

print(sum(numbers))