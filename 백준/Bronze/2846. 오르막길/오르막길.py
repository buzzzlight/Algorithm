N = int(input())
road = list(map(int, input().split()))
total = 0
upp = []

for i in range(0, N - 1):
    if road[i] < road[i + 1]:
        total += road[i + 1] - road[i]
    else:
        upp.append(total)
        total = 0

upp.append(total)

print(max(upp))