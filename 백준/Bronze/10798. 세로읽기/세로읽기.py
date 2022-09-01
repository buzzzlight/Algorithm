list_ = []

for i in range(5):
    list_.append([0]*15)

for i in range(5):
    d = list(input())
    for j in range(len(d)):
        list_[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if list_[j][i] == 0:
            continue;
        else:
            print(list_[j][i], end='')