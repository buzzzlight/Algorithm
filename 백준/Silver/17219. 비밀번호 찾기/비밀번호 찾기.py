n, m = map(int, input().split())
dic = {}

for i in range(n):
    address, password = input().split()
    dic[address] = password

for i in range(m):
    q = input()
    print(dic[q])