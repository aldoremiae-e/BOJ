C, N = map(int, input().split())
memo = [0] + [int(1e7)] * (C + 100)
info = [list(map(int, input().split())) for _ in range(N)]

for c, n in info:
    for i in range(n, C+101):
        memo[i] = min(memo[i], memo[i-n] + c)
print(min(memo[C:C+101]))
