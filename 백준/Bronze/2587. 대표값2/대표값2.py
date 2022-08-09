numbers = []

for i in range(5):
    numbers.append(int(input()))

a = sum(numbers) // 5
b = sorted(numbers)[2]

print(a, b, sep='\n')