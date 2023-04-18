n = int(input())
time = list(map(int, input().split()))

time.sort()
answer = 0

for i in range(1, n + 1):
    answer += sum(time[:i])

print(answer)