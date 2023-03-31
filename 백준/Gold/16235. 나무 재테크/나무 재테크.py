from collections import deque
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def ssfw():
    global trees, maps
    new_trees = deque()
    five_trees = deque()
    new_maps = [[0] * N for _ in range(N)]
    for tree in trees:
        stx, sty, told = tree[0], tree[1], tree[2]
        if maps[stx][sty] >= told:
            maps[stx][sty] -= told
            new_trees.append((stx, sty, told+1))
            if (told + 1) % 5 == 0:
                five_trees.append((stx, sty))
        else:
            new_maps[stx][sty] += int(told // 2)
    # 죽은 나무 양분이 됨
    trees = new_trees
    birth = deque()

    for tree in five_trees:
        ftx, fty = tree[0], tree[1]
        for di, dj in dirs:
            ci, cj = di + ftx, dj + fty
            if 0 <= ci < N and 0 <= cj < N:
                birth.append((ci, cj, 1))
    for t in birth:
        trees.appendleft(t)

    # 양분 추가
    for i in range(N):
        for j in range(N):
            maps[i][j] += (add_maps[i][j] + new_maps[i][j])
    return
N, M, K = map(int, input().split())
maps = [[5] * N for _ in range(N)]
add_maps = [list(map(int, input().split())) for _ in range(N)]
trees = deque()
for _ in range(M):
    x, y, z = map(int, input().split())
    trees.append((x-1, y-1, z))

for _ in range(K):
    ssfw()
print(len(trees))