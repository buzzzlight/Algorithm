a = int(input())
total = 0
n = 0

while True:
    n += 1
    total += n
    if total >= a:
        break

print(n)