import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stack = []
cnt = 0

for i in range(M):
    k = int(input())
    k1 = list(map(int, input().split()))
    for n in range(1, k):
        cnt += 1
        if k1[n - 1] > k1[n]:
            stack.append('Yes')

if len(stack) == cnt:
    print('Yes')
else:
    print('No')