for _ in range(10):
    T = int(input())
    numbers = list(map(int, input().split()))
    while numbers[-1] > 0:
        for i in range(5):
            numbers.append(numbers[0] - (i + 1))
            numbers.pop(0)
            if numbers[-1] <= 0:
                break
    numbers[-1] = 0
    numbers = ' '.join(map(str, numbers))

    print(f'#{T} {numbers}')