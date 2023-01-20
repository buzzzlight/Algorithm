A, B = map(int, input().split())
C = int(input())
hour = (B + C) // 60
min = (B + C) % 60

if hour == 0:
    print(A, B + C)
else:
    if A + hour > 23:
        A = A + hour - 24
        print(A, min)
    else:
        print(A + hour, min)
