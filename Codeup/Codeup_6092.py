student = [0] * 24
n = int(input())
check = list(map(int, input().split()))

for i in check:
    student[i] += 1

print(*student[1:])