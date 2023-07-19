N, M = map(int, input().split())
lst = []
def dfs(m):
    if m == M:
        print(*lst)
        return
    for i in range(1, N+1):
        if i in lst:
            continue
        lst.append(i)
        dfs(m+1)
        lst.pop()
dfs(0)