N = int(input())
list_ = []

for i in range(N):
    list_.append(list(map(int, input().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if list_[i][0] < list_[j][0] and list_[i][1] < list_[j][1]:
            rank += 1
    print(rank, end=' ')