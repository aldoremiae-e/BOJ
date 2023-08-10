T = int(input())
memo = [0] * (1000001)
memo[1] = 1
memo[2] = 2
memo[3] = 4
for _ in range(T):
    N = int(input())
    for i in range(4, N+1):
        if memo[i] == 0:
            memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % 1000000009
    print(memo[N])