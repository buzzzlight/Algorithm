P, K = map(int, input().split())
cnt = 0

while K != P:
    cnt += 1
    K +=1

print(cnt + 1)