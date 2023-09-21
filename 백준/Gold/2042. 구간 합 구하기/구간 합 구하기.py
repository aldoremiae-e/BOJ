from math import ceil, log
N, M, K = map(int, input().split())
arr = [0] * N
# h 트리의 높이, 노드의 개수 2 ** (h+1)
h = ceil(log(N, 2))
tree = [0] * (2 ** (h+1))
leaf = {}
for i in range(N):
    tree[2**h + i] = int(input())
    leaf[i] = 2**h + i
# bot-up dp를 활용한 부분합 tree 만들기
def trees():
    global tree
    for i in range(2**h -1 , 0, -1):
        # 부모노드는 자식노드 왼쪽 + 자식노드 오른쪽
        tree[i] = tree[i*2] + tree[i*2+1]
def change(cur_node, diff):
    global tree
    if cur_node == 0:
        return
    tree[cur_node] += diff
    change(cur_node//2, diff)
def solve(l, r, node):
    # b, c가 있으면
    if c < l or r < b:
        return 0
    if b <= l and r <= c:
        return tree[node]
    mid = (l + r) // 2
    ans = solve(l, mid, node*2) + solve(mid+1, r, node*2 + 1)
    return ans
trees()

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        # b번째 수를 c로 바꾸기
        cur_node = leaf[b-1]
        diff = c - tree[cur_node]
        change(cur_node, diff)
    else:
        # b부터 c까지 구간합 구하기
        print(solve(1, 2**h, 1))