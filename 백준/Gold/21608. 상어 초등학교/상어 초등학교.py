# 순서 - 4명
# abs(r1-r2) + abs(c1-c2) == 1 상하좌우
from copy import deepcopy
from collections import deque
def first(std):
    global q
    love_blank = [[0] * N for _ in range(N)]
    max_num = -1
    fi, fj = 0, 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                for di, dj in dir:
                    ci, cj = i + di, j + dj
                    if 0 <= ci < N and 0 <= cj < N:
                        if maps[ci][cj] in fav[std]:
                            love_blank[i][j] += 10
                        elif maps[ci][cj] == 0:
                            love_blank[i][j] += 1
                if max_num < love_blank[i][j]:
                    fi, fj = i, j
                    max_num = love_blank[i][j]
    maps[fi][fj] = std

def score(si, sj):
    num = 0
    for di, dj in dir:
        ci, cj = si + di, sj + dj
        if 0 <= ci < N and 0 <= cj < N and maps[ci][cj] in fav[maps[si][sj]]:
           num += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 10
    elif num == 3:
        return 100
    elif num == 4:
        return 1000

N = int(input())
maps = [[0] * N for _ in range(N)]
fav = {}
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for k in range(N ** 2):
    n, a, b, c, d = map(int, input().split())
    fav[n] = tuple((a, b, c, d))
    if k == 0:
        maps[1][1] = n
flag = 0
for key, val in fav.items():
    if flag == 0:
        flag = 1
        continue
    first(key)
ans = 0
for i in range(N):
    for j in range(N):
        ans += score(i, j)

print(ans)