n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]

def count(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                count(x, y, n // 2)
                count(x, y + n // 2, n // 2)
                count(x + n // 2, y, n // 2)
                count(x + n // 2, y + n // 2, n // 2)
                return 0
            
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1

count(0, 0, n)
print(answer[0])
print(answer[1])