N = int(input())
first = N
cnt = 0

while True:
    if N < 10:
        numbers = '0' + str(N)
        new = int(numbers[0]) + int(numbers[1])
        if new < 10:
            N = int(numbers[1]) * 10 + new
            cnt += 1
            if N == first:
                break
        else:
            new = list(str(new))
            N = int(numbers[1]) * 10 + int(new[1])
            cnt += 1
            if N == first:
                break
    else:
        numbers = list(str(N))
        new = int(numbers[0]) + int(numbers[1])
        if new < 10:
            N = int(numbers[1]) * 10 + new
            cnt += 1
            if N == first:
                break
        else:
            new = list(str(new))
            N = int(numbers[1]) * 10 + int(new[1])
            cnt += 1
            if N == first:
                break

print(cnt)