from sys import stdin
from collections import deque

N = int(stdin.readline())
tri = list(list(map(int, stdin.readline().split()))for _ in range(N))
dp = list([0] * (i+1) for i in range(N))
dp[0][0] = tri[0][0]
if N > 1:
    dp[1][0] = dp[0][0] + tri[1][0]
    dp[1][1] = dp[0][0] + tri[1][1]
    K = 3
    for i in range(2, N):
        for j in range(K):
            if j == 0:
                dp[i][j] = tri[i][j] + dp[i-1][j]
            elif j == (K-1):
                dp[i][j] = tri[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = tri[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        K += 1
print(max(dp[N-1]))