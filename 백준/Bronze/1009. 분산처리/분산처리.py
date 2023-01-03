T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    b = b % 4
    if b == 0:
        b = 4
    number = (a**b) % 10
    if number == 0:
        print(10)
    else:
        print(number)
