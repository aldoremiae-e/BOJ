from heapq import heappop, heappush

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    birth = []
    # 봄 + 가을
    for i in range(N):
        for j in range(N):
            new_tree = []
            trees[i][j].sort()
            dead = 0
            for z in trees[i][j]:
                if B[i][j] >= z:
                    B[i][j] -= z
                    new_tree.append(z+1)
                    if (z+1) % 5 == 0:
                        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                            nx, ny = i + dx, j + dy
                            if not (0 <= nx < N and 0 <= ny < N):
                                continue
                            birth.append((nx, ny))
                else:
                    dead += z//2
            trees[i][j] = new_tree
            B[i][j] += dead + A[i][j]

    while birth:
        i, j = birth.pop()
        trees[i][j].append(1)
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])
print(ans)