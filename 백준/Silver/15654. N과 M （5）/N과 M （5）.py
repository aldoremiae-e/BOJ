from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
nums = sorted(list(map(int, stdin.readline().split())))
lst = deque()
visited = [0] * N
def dfs(cnt):
    if cnt == M:
        print(*lst)
        return
    for i in range(N):
        if visited[i] == 0:
            lst.append(nums[i])
            visited[i] = 1
        else:
            continue
        cnt += 1
        dfs(cnt)
        cnt -= 1
        visited[i] = 0
        lst.pop()
dfs(0)