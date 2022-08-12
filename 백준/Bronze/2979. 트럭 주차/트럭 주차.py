A, B, C = map(int, input().split())
time = [0] * 100

for i in range(3):
    a, b = map(int, input().split())
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for j in range(a, b):
        time[j] += 1

for k in time:
    if k == 1:
        cnt_1 += 1
    elif k == 2:
        cnt_2 += 1
    elif k == 3:
        cnt_3 += 1

# 주차요금 * 시간 * 자동차 수
print(cnt_1 * A + cnt_2 * B * 2 + cnt_3 * C * 3)