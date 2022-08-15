A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
cnt_A = 0
cnt_B = 0
list_ = []

for i in range(10):
    if A_list[i] > B_list[i]:
        list_.append('A')
        cnt_A += 3
    elif A_list[i] < B_list[i]:
        list_.append('B')
        cnt_B += 3
    else:
        list_.append('D')
        cnt_A += 1
        cnt_B += 1
print(cnt_A, cnt_B)

if A_list == B_list:
    print('D')
elif cnt_A > cnt_B:
    print('A')
elif cnt_A < cnt_B:
    print('B')
elif cnt_A == cnt_B:
    while 'D' in list_:
        list_.remove('D')
    print(list_[-1])