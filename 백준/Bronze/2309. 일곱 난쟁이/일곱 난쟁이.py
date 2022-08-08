tall = []

for i in range(9):
    tall.append(int(input()))
total = sum(tall)

for j in range(8):
    for k in range(j + 1, 9):
        fakes = tall[j] + tall[k]
        if total - fakes == 100:
            tall.pop(k)
            tall.pop(j)
            break
    if len(tall) == 7:
        break

for _ in sorted(tall):
    print(_)