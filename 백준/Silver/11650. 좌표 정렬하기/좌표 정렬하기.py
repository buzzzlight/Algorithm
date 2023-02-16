N = int(input())
loc = []

for _ in range(N):
    loc.append(list(map(int, input().split())))

loc.sort(key=lambda x:x[1])
loc.sort(key=lambda x:x[0])

for i in range(N):
    print(loc[i][0], loc[i][1])