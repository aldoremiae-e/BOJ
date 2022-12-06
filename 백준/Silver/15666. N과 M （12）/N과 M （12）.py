from sys import stdin

N, M = map(int, stdin.readline().split())
nums = sorted((list(map(int, stdin.readline().split()))))
lst, ans = [], set()
visited = [0] * N
def dfs(cnt, idx):
    if cnt == M:
        # TypeError: unhashable type: 'list'
        ans.add(tuple(lst))
        return
    for i in range(idx, N):
        if visited[i] <= M:
            lst.append(nums[i])
            visited[i] += 1
        cnt += 1
        dfs(cnt, i)
        cnt -= 1
        visited[i] -= 1
        lst.pop()
dfs(0, 0)
for i in ans:
    print(*i)