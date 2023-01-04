# 트리 순회
from sys import stdin
N = int(stdin.readline())
tree = {}
visit = {}
for _ in range(N):
    parent, left, right = map(str, stdin.readline().split())
    tree[parent] = (left, right)
    visit[parent] = 0
def front(root, left, right):
    global visit
    print(root, end='')
    visit[root] = 1
    if left != '.' and visit[left] == 0:
        front(left, tree[left][0], tree[left][1])

    if right != '.' and visit[right] == 0:
        front(right, tree[right][0], tree[right][1])

def mid(root, left, right):
    global visit
    if left != '.' and visit[left] == 0:
        mid(left, tree[left][0], tree[left][1])
    print(root, end='')
    visit[root] = 1
    if right != '.' and visit[right] == 0:
        mid(right, tree[right][0], tree[right][1])

def post(root, left, right):
    global visit
    if left != '.' and visit[left] == 0:
        post(left, tree[left][0], tree[left][1])
    if right != '.' and visit[right] == 0:
        post(right, tree[right][0], tree[right][1])
    print(root, end='')
    visit[root] = 1

front('A', tree['A'][0], tree['A'][1])
print()
for key, val in visit.items():
    visit[key] = 0
mid('A', tree['A'][0], tree['A'][1])
print()
for key, val in visit.items():
    visit[key] = 0
post('A', tree['A'][0], tree['A'][1])
