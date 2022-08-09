n = int(input())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0:
        if y > 0:
            Q1 += 1
        else:
            Q4 += 1
    elif x < 0:
        if y > 0:
            Q2 += 1
        else:
            Q3 += 1

print('Q1:', Q1)
print('Q2:', Q2)
print('Q3:', Q3)
print('Q4:', Q4)
print('AXIS:', AXIS)
