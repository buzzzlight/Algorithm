exp = input().split("-")
nums = []

for i in exp:
    num = i.split("+")
    sum = 0
    for j in num:
        sum += int(j)
    nums.append(sum)

answer = nums[0]

for i in range(1, len(nums)):
    answer -= nums[i]

print(answer)