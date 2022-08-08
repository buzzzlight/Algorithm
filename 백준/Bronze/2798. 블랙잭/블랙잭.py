N, M = map(int, input().split())
card = list(map(int, input().split()))
max_ = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = card[i] + card[j] + card[k]
            if max_ < total <= M:
                max_ = total
                if max_ == M:
                    break

print(max_)
