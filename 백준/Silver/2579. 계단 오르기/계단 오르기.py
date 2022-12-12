from sys import stdin
N = int(stdin.readline())
dp = [0] * N
arr = [0] * N
for i in range(N):
    arr[i] = int(stdin.readline())
    
dp[0] = arr[0]
if N > 1:
    dp[1] = arr[0] + arr[1]
    if N > 2:
        dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
print(dp[N-1])