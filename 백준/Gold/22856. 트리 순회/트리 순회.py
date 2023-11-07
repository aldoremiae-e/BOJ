import sys
sys.setrecursionlimit(int(1e8))
N = int(input())
trees = {}
for _ in range(N):
    a, b, c = map(int, input().split())
    trees[a] = (b, c)

def inorder(n):
    global inorder_lst
    if trees[n][0] != -1:
        inorder(trees[n][0])
    inorder_lst.append(n)
    if trees[n][1] != -1:
        inorder(trees[n][1])

def similar(n, cnt):
    global flag
    ret = cnt
    if trees[n][0] != -1:
        ret = similar(trees[n][0], ret+1)
    if n == inorder_lst[-1]:
        print(ret)
        exit()
    if trees[n][1] != -1:
        ret = similar(trees[n][1], ret+1)
    return ret+1

flag = False
inorder_lst = []
inorder(1)
similar(1, 0)