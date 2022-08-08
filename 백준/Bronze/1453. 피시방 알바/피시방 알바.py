N = int(input())
seat = list(map(int, input().split()))
seat2 = []
cnt = 0

for i in range(N):
    if seat[i] not in seat2:
        seat2.append(seat[i])
    elif seat[i] in seat2:
        cnt += 1

print(cnt)