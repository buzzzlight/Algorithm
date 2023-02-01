N = int(input())
numbers = set(map(int, input().split()))
M = int(input())
numbers2 = list(map(int, input().split()))

for i in numbers2:
    if i in numbers:
        print(1)
    else:
        print(0)