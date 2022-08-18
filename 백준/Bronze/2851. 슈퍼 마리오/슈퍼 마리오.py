mushroom = []
total = 0
total_list = []

for i in range(10):
    mushroom.append(int(input()))

for i in mushroom:
    total += i
    total_list.append(total)
    if total > 100:
        break

a = total_list[-1] - 100
b = 100 - total_list[-2]
if a > b:
    print(total_list[-2])
elif a < b:
    print(total_list[-1])
else:
    print(max(total_list[-1], total_list[-2]))