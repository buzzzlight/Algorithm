T = int(input())

for i in range(T):
    score = list(map(int, input().split()))
    score_avg = sum(score[1:])/score[0]
    student = 0
    for j in range(1, len(score)):
        if score[j] > score_avg:
            student += 1
    print('%.3f'%round(student/score[0]*100, 3), '%', sep='')