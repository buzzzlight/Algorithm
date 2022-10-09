N = int(input())
card = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

dic = {}

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in card2:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")