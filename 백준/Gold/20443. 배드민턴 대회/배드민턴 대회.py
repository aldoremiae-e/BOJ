N = int(input())
def comb(n, r):
    m = 1
    k = 1
    while r >= 1:
        m *= n
        k *= r
        r -= 1
        n -= 1
    return (m // k)

dp = [0] * ((4 * (N//4)) +1)
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 2
dp[4] = 9

for i in range(5, len(dp)):
    # 교란순열의 점화식 (수학하)
    dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % 1000000007

t = comb(N, N % 4)
print((dp[(N//4) * 4] * t) % 1000000007)