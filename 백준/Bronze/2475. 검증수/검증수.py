numbers = map(int, input().split())
sqr_sum = 0

for i in numbers:
    sqr_sum += i**2

print(sqr_sum % 10)