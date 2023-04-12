n = int(input())
result = 1

for i in range(1, n + 1):
    result *= i

result_reverse = str(result)[::-1]
cnt = 0

for j in result_reverse:
    if j == '0':
        cnt += 1
    else:
        print(cnt)
        break