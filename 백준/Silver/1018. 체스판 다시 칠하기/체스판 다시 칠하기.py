N, M = map(int, input().split())
chess = []
cnt = []

for _ in range(N):
    chess.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        white = 0   # 시작점이 흰색일때
        black = 0   # 시작점이 검정색일때
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if chess[a][b] != 'W':
                        black += 1
                    if chess[a][b] != 'B':
                        white += 1
                else:
                    if chess[a][b] != 'B':
                        black += 1
                    if chess[a][b] != 'W':
                        white += 1
        cnt.append(min(white, black))

print(min(cnt))