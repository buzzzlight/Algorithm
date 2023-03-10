l = int(input())
word = input()
numbers = []
cnt = 0
ans = 0

for i in word:
    num = ord(i) - 96
    numbers.append(num)

for j in numbers:
    ans += j * (31 ** cnt)
    cnt += 1

print(ans)