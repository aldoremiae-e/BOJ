import sys
sys.setrecursionlimit(int(1e5))

N = int(input())
dic = {}
for _ in range(N-1):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = []
    if b not in dic:
        dic[b] = []
    dic[a].append(b)
    dic[b].append(a)

def find_depth(node, d):
    global visit, parent, depth
    visit[node] = 1
    depth[node] = d
    for child in dic[node]:
        if visit[child] == 1:
            continue
        parent[child] = node
        find_depth(child, d+1)

def lca(a, b):
    if depth[a] <= depth[b]:
        i, j = a, b
    else:
        i, j = b, a
    while depth[i] != depth[j]:
        j = parent[j]
    # 부모를 맞춰
    while i != j:
        i = parent[i]
        j = parent[j]
    return i

depth = [0] * (N+1) # 깊이를 저장
parent = [0] * (N+1) # 부모를 저장
visit = [0] * (N+1) # 깊이찾는 dfs 방문처리
find_depth(1, 0) # 루트부터 내려가는 방식

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))