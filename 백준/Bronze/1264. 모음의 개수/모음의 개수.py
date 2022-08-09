list_ = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    s = input()
    cnt = 0
    if s == '#':
        break
    else:
        for i in s:
            if i in list_:
                cnt += 1
        print(cnt)