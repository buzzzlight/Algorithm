t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1 or n == 2:
        print(n)
    elif n == 3:
        print(4) 
    else:
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 4

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        print(dp[n])