T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(1, T + 1):
    N, K = map(int, input().split())
    score_list = []
    total = []
    for j in range(1, N + 1):
        score = list(map(int, input().split()))
        score_list.append(score)
        total.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)
    
    K_total = total[K- 1]
    total.sort(reverse = True)
    K_score = total.index(K_total) // (N // 10)
    print(f'#{i} {grade[K_score]}')