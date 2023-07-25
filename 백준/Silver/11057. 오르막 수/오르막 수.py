n = int(input())

memo = [[0] * 11 for _ in range(n+1)]
memo[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, n+1):
    for j in range(1, 11):
        memo[i][j] = (memo[i][j-1] + memo[i-1][j]) % 10007
print(memo[-1][-1])