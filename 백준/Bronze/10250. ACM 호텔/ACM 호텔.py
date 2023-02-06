T = int(input())

# N // H + 1 == 호 수
# N % N == 층 수

for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        print(H * 100 + N // H)
    else:
        print(N % H * 100 + N // H + 1)