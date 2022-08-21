N, M = map(int, input().split())
listen = set()
see = set()

for i in range(N):
    listen.add(input())

for j in range(M):
    see.add(input())

both = sorted(list(listen & see))

print(len(both), *both, sep='\n')