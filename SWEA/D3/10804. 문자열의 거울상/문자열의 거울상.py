T = int(input())

for i in range(1, T + 1):
    str = input()
    str_reverse = str[::-1]
    mirror = ''
    for j in str_reverse:
        if j == 'b':
            mirror += 'd'
        elif j == 'd':
            mirror += 'b'
        elif j == 'p':
            mirror += 'q'
        else:
            mirror += 'p'
    print(f'#{i} {mirror}')