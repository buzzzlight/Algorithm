import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(nums, x)
    else:
        if nums:
            print(heapq.heappop(nums))
        else:
            print(0)