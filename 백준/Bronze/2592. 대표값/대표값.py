list_ = []
for i in range(10):
    list_.append(int(input()))

list_set = list(set(list_))
cnt_list = []

for j in list_set:
    cnt = list_.count(j)
    cnt_list.append(cnt)

print(int(sum(list_)/10))
print(list_set[cnt_list.index(max(cnt_list))])
