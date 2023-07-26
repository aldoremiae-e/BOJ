N = int(input())
lst = list(map(int, input().split()))
memo = [1] * N
for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]:
            memo[i] = max(memo[j]+1, memo[i])
print(max(memo))
ans = []
k = max(memo)
for i in range(N-1, -1, -1):
    if memo[i] == k:
        ans.append(lst[i])
        k -= 1
ans.reverse()
print(*ans)