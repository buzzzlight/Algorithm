T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    people = []
    for i in range(1, n + 1):
        people.append(i)
    
    if k == 0:
        print(people[-1])
    else:
        for j in range(k):
            for k in range(1, n):
                people[k] += people[k-1]
        print(people[-1])
