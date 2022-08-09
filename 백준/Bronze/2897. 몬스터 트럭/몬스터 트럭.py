# # R, C = 행, 열 개수
# R, C = map(int, input().split())
# parking = []

# for i in range(R):
#     parking.append(list(input()))

R, C = 4, 4
parking = [
    ['#','.','.','#'],
    ['.','.','X','.'],
    ['.','.','X','.'],
    ['#','X','X','#']
]

# 차 0~4대를 부수고 주차할 수 있는 공간의 개수 count변수
cnt = [0, 0, 0, 0, 0]

for i in range(R - 1):
    for j in range(C - 1):
        # 2 X 2 공간 순회
        a = parking[i][j]
        b = parking[i][j + 1]
        c = parking[i + 1][j]
        d = parking[i + 1][j + 1]
        space = a + b + c + d
    
        if "#" in space:
            continue
        else:
            car = space.count("X")
            if car == 0:
                cnt[0] += 1
            if car == 1:
                cnt[1] += 1
            if car == 2:
                cnt[2] += 1
            if car == 3:
                cnt[3] += 1
            if car == 4:
                cnt[4] += 1

for i in cnt:
    print(i)
