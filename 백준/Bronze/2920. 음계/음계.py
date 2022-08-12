list_ = list(map(int, input().split()))

list_ascending = []
for i in range(1, 9):
    list_ascending.append(i)

list_descending = []
for i in range(8, 0, -1):
    list_descending.append(i)

if list_ == list_ascending:
    print('ascending')
elif list_ == list_descending:
    print('descending')
else:
    print('mixed')