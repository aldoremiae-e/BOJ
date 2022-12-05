from sys import stdin
N, M = map(int, stdin.readline().split())
lst = [0] * N
def dfs(cnt, idx):
    if cnt == M:
        for i, v in enumerate(lst):
            if v:
                for n in range(v):
                    print(i+1, end=' ')
        print()
        return
    for i in range(idx, N):
        lst[i] += 1
        cnt += 1
        dfs(cnt, i)
        cnt -= 1
        lst[i] -= 1
dfs(0,0)