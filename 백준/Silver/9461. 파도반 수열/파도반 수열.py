from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    if N <= 5:
        dp = [0] * 5
        dp[0], dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2, 2
    else:
        dp = [0] * N
        dp[0], dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2, 2
        for i in range(5, N):
            dp[i] = dp[i-1] + dp[i-5]

    print(dp[N-1])