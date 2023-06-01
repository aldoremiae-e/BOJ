import sys
sys.setrecursionlimit(10**5 + 10)
N = int(input())
# 왼 루 오
inorder = list(map(int, input().split()))
# 왼 오 루
# 포스트오더의 마지막은 무조건 루트야!
postorder = list(map(int, input().split()))
# 루 왼 오
preorder = []
def pre(i_start, i_end, p_start, p_end):
    if (i_start > i_end) or (p_start > p_end):
        return
    if i_start == i_end or p_start == p_end:
        preorder.append(postorder[p_end])
        return
    root = postorder[p_end]
    target = inorder.index(root)
    preorder.append(root)
    # 왼쪽 트리 개수
    left_tree_cnt = target - i_start
    # 오른쪽 트리 개수
    right_tree_cnt = i_end - target
    pre(i_start, target-1, p_start, p_start + left_tree_cnt - 1)
    pre(target+1, i_end, p_end - right_tree_cnt, p_end-1)
pre(0, N-1, 0, N-1)
print(*preorder)