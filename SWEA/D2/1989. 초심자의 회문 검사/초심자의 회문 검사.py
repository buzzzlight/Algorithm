T = int(input())

for test_case in range(1, T + 1):
    str = input()
    if str == str[::-1]:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')