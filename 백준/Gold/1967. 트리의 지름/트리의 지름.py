from sys import stdin
import sys
sys.setrecursionlimit(10 ** 9)
N = int(stdin.readline())
tree = [[] for _ in range(N)]

for i in range(N-1):
    p, s, v = map(int, stdin.readline().split())
    tree[p-1].append((s-1, v))
    tree[s-1].append((p-1, v))

def dfs(cur, d):
    for s, v in tree[cur]:
        if visit[s] == -1:
            visit[s] = d + v
            dfs(s, d + v)

visit = [-1] * N
visit[0] = 0
dfs(0, 0)

start = visit.index(max(visit))
visit = [-1] * N
visit[start] = 0
dfs(start, 0)
print(max(visit))