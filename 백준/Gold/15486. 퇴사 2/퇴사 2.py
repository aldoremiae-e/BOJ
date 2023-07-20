N = int(input())
works = [(0, 0)]
for _ in range(N):
    works.append(tuple(map(int, input().split())))
memo = [0 for _ in range(N+2)]
for i in range(1, N+1):
    memo[i] = max(memo[i], memo[i-1])
    t, p = works[i][0], works[i][1]
    next_day = i + t
    if next_day <= N+1:
        memo[next_day] = max(memo[next_day], p+memo[i])

memo[N+1] = max(memo[N+1], memo[N])
print(memo[N+1])
