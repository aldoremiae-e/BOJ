from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
nums = sorted(list(map(int, stdin.readline().split())))
lst = deque()
visited = [0] * N
ans = deque()
def dfs(cnt, idx):
    global ans
    if cnt == M:
        print(*lst)
        return
    for i in range(N):
        if i >= idx and visited[i] <= M:
            lst.append(nums[i])
            visited[i] += 1
        else:
            continue
        cnt += 1
        dfs(cnt, i)
        cnt -= 1
        visited[i] -= 1
        lst.pop()
dfs(0, 0)