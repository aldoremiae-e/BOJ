from pprint import pprint
from collections import deque
from copy import deepcopy
def game(Cmaps):
    for j in range(1, N+1):
        # 현재 위치
        ci, cj = 1, j
        # 한 칸씩 내려가면서 확인 할 것
        for i in range(1, H+1):
            if Cmaps[i][cj] == 1: #오른쪽이동
                cj += 1
            elif Cmaps[i][cj-1] == 1: #왼쪽이동
                cj -= 1
        # cj 도착했을 때의 위치
        if j == cj:
            continue
        else:
            return -1
    # 1부터 N까지 다 같을 떄
    return 1

def dfs(Cnt, Cmaps, li, lj):
    global ans
    if Cnt > 3:
        return

    ret = game(Cmaps)
    if ret > 0:
        ans = min(ans, Cnt)
        return

    for i in range(li, H+1):
        for j in range(lj, N):
            if Cmaps[i][j] == 0 and Cmaps[i][j-1] == 0 and maps[i][j+1] == 0:
                # 사다리를 넣고
                Cmaps[i][j] = 1
                dfs(Cnt+1, Cmaps, i, j)
                Cmaps[i][j] = 0
        lj = 0

N, M, H = map(int, input().split())
maps = [[0] * (N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())
    maps[a][b] = 1
ans = 4
dfs(0, maps, 1, 1)
if ans == 4:
    print(-1)
else:
    print(ans)