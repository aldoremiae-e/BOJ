import sys
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline
N = int(input())
tree = {}
for _ in range(N-1):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = []
    if b not in tree:
        tree[b] = []
    tree[a].append(b)
    tree[b].append(a)
def dp(n):
    global visit, memo
    visit[n] = True
    for child in tree[n]:
        if visit[child]:
            continue
        dp(child)
        # 자식이 얼리어답터이어야함
        memo[n][0] += memo[child][1]
        # 부모가 얼리어답터일때 자식은 상관없음
        memo[n][1] += min(memo[child])

# 얼리어답터 일때 아닐때
memo = [[0, 1] for _ in range(N+1)]
visit = [False for _ in range(N+1)]

dp(1)
print(min(memo[1]))