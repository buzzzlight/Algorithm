n, m = map(int, input().split())
pocketmon_num = {}
num_pocketmon = {}

for i in range(1, n + 1):
    name = input()
    pocketmon_num[name] = i
    num_pocketmon[i] = name

for i in range(m):
    q = input()
    if q.isdigit():
        print(num_pocketmon[int(q)])
    else:
        print(pocketmon_num[q])