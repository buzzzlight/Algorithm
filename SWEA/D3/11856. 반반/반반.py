TC = int(input())

for i in range(1, TC + 1):
    S = input()
    list_ = list(S)
    list_2 = list(set(list(S)))
    cnt = 0
    cnt_2 = 0
    if len(list_2) == 2:
        for j in range(len(list_)):
            if list_[j] == list_2[0]:
                cnt += 1
            elif list_[j] == list_2[1]:
                cnt_2 += 1
            if cnt == 2 and cnt_2 == 2:
                print(f'#{i} Yes')            
    else:
        print(f'#{i} No')