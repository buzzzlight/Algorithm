a, b, c = map(int, input().split())
cnt = 1

while cnt % a != 0 or cnt % b != 0 or cnt % c != 0:
    cnt += 1

print(cnt)