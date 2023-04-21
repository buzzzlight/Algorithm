import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sums = [0] * (n + 1) # 누적합 리스트

for i in range(1, n + 1):
    sums[i] = sums[i - 1] + numbers[i - 1]

for _ in range(m):
    a, b = map(int, input().split())
    print(sums[b] - sums[a - 1])