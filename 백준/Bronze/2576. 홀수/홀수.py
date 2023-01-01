numbers = []
odd = []

for i in range(7):
    numbers.append(int(input()))

for i in numbers:
    if i % 2 == 1:
        odd.append(i)

if len(odd) == 0:
    print('-1')
else:
    print(sum(odd), min(odd), sep='\n')