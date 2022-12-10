from sys import stdin
from collections import deque
N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
q = deque()
dp = [list([0] * 3) for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]

for i in range(1, N):
    dp[i][0] = arr[i][0] + dp[i-1][1] if dp[i-1][1] < dp[i-1][2] else arr[i][0] + dp[i-1][2]
    dp[i][1] = arr[i][1] + dp[i-1][0] if dp[i-1][0] < dp[i-1][2] else arr[i][1] + dp[i-1][2]
    dp[i][2] = arr[i][2] + dp[i-1][0] if dp[i-1][0] < dp[i-1][1] else arr[i][2] + dp[i-1][1]

print(min(dp[N-1]))