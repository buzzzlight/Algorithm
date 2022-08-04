N = int(input())
room = []
for i in range(N):
    room.append(list(input()))

trans_room = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        trans_room[i][j] = room[j][i]

w2 = 0
h2 = 0

for i in range(N):
    w = 0
    for j in range(N):
        if room[i][j] == '.':
            w += 1
            if w == 2:
                w2 += 1
        elif room[i][j] == 'X':
            w = 0

for i in range(N):
    h = 0
    for j in range(N):
        if trans_room[i][j] == '.':
            h += 1
            if h == 2:
                h2 += 1
        elif trans_room[i][j] == 'X':
            h = 0

print(w2, h2)