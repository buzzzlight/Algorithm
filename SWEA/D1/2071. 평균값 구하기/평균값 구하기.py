T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print(f'#{test_case} {round(sum(numbers)/10)}')