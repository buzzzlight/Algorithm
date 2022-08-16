T = int(input())

for i in range(1, T + 1):
    list_ = list(map(int, input().split()))
    print(f'#{i} {max(list_)}')