n = int(input())
nums = list(map(int, input().split()))

nums2 = sorted(set(nums))

dict = {}
for i in range(len(nums2)):
    dict[nums2[i]] = i

for i in nums:
    print(dict[i], end=' ')