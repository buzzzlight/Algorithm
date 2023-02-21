import sys
from collections import Counter

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

print(round(sum(numbers) / n))
print(numbers[(n - 1) // 2])

cnt = Counter(numbers).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(numbers) - min(numbers))