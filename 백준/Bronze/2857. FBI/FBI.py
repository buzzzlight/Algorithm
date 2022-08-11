agent = []

for i in range(5):
    agent.append(input())

for j in range(5):
    if 'FBI' in agent[j]:
        print(j + 1, end=' ')
        agent[j] = 0

if agent.count(0) == 0:
    print("HE GOT AWAY!")
