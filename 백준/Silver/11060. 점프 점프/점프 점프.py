N = int(input())
lst = list(map(int, input().split()))

memo = [-1] * N
memo[0] = 0
for i in range(N):
    if memo[i] == -1:
        continue
    for j in range(1, lst[i]+1):
        if i+j == N:
            break
        if memo[i+j] != -1:
            memo[i+j] = min(memo[i+j], memo[i] + 1)
        else:
            memo[i+j] = memo[i] + 1
print(memo[N-1])