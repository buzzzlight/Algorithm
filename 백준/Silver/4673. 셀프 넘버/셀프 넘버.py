self_num = []

for i in range(1, 10001):
    a = i
    while a > 0:
        i += a % 10
        a = a // 10
    self_num.append(i)

for i in range(1, 10001):
    if i not in self_num:
        print(i)
