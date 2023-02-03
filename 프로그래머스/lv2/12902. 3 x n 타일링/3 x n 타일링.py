def solution(n):
    answer = 0
    dp = [0] * (n//2)
    dp[0] = 3
    dp[1] = 11
    if n// 2 > 1:
        for i in range(2, n//2):
            dp[i] = (dp[i-1] * 3 + 2) % 1000000007
            for j in range(i-1):
                dp[i] = (dp[i] + dp[j] * 2) % 1000000007
    answer = dp[n//2 - 1]
    return answer