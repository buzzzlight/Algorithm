R, C = map(int, input().split())
parking = []

for i in range(R):
    parking.append(list(input()))

# R, C = 4, 4
# parking = [
#     ['#','.','.','#'],
#     ['.','.','X','.'],
#     ['.','.','X','.'],
#     ['#','X','X','#']
# ]

cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0

for i in range(R):
    for j in range(C):
        if i + 1 == R or j + 1 == C:
            break
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
                cnt_0 += 1
            if car == 1:
                cnt_1 += 1
            if car == 2:
                cnt_2 += 1
            if car == 3:
                cnt_3 += 1
            if car == 4:
                cnt_4 += 1

print(cnt_0)
print(cnt_1)
print(cnt_2)
print(cnt_3)
print(cnt_4)