N = int(input())
member = []

for _ in range(N):
    member.append(list(input().split()))

member.sort(key=lambda x:int(x[0]))

for i in range(N):
    print(member[i][0], member[i][1])