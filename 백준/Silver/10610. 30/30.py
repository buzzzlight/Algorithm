N = input()
number = list(N)

if '0' not in number:
    print(-1)

else:
    number = list(map(int, number))
    if sum(number) % 3 == 0:
        number.sort(reverse=True)
        print(*number, sep='')
    else:
        print(-1)
