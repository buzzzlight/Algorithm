N = int(input())
bag = 0

while N >= 0:
    if N % 5 == 0:
        print(bag + N // 5)
        break
    N -= 3
    bag += 1
else:
    print(-1)