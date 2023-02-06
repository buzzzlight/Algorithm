n, k = map(int, input().split())
nf = 1
kf = 1
nkf = 1

for i in range(1, n + 1):
    nf *= i

for i in range(1, k + 1):
    kf *= i

for i in range(1, n - k + 1):
    nkf *= i

print(int(nf / (kf * nkf)))