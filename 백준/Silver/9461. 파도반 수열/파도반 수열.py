t = int(input())

for _ in range(t):
    n = int(input())
    if n < 4:
        print(1)
    else:
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 1, 1

        for i in range(4, n + 1):
            dp[i] = dp[i - 2] + dp[i - 3]

        print(dp[n])