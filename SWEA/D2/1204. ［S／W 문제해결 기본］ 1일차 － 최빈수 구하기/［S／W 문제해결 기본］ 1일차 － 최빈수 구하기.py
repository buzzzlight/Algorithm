T = int(input())

for i in range(T):
    test_case = input()
    score = list(input().split())
    score_set = list(set(score))
    cnt_list = []
    for j in score_set:
        cnt = score.count(j)
        cnt_list.append(cnt)

    print(f'#{test_case} {score_set[cnt_list.index(max(cnt_list))]}')