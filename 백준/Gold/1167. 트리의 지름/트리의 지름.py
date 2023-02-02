from sys import stdin
V = int(stdin.readline())
tree = [[] for _ in range(V)]
# 인풋
for _ in range(V):
    input = list(map(int, stdin.readline().split()))
    i = input[0] - 1
    lst = []
    for k in range(1, len(input)-1, 2):
        j = input[k] - 1
        v = input[k+1]
        tree[i].append((j, v))
#dfs
def dfs(i, d):
    for x, v in tree[i]:
        if visit[x] == -1:
            visit[x] = v + d
            dfs(x, v + d)
#인풋노드 돌기
ans = 0
visit = [-1] * V
visit[0] = 0
dfs(0, 0)
start = visit.index(max(visit))
visit = [-1] * V
visit[start] = 0
dfs(start, 0)
print(max(visit))