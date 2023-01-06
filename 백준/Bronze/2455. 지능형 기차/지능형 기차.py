number = []
people = 0

for _ in range(4):
    a, b = map(int, input().split())
    people = people - a + b
    number.append(people)
    
print(max(number))