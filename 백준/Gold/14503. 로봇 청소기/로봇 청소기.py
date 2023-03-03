from sys import stdin
from collections import deque
def clean(si, sj, sd, cnt):
    global visit, ans, dir_z, dir_f, dir_s, dir_t, flag2

    if ans < cnt:
        ans = cnt
    # 1
    if visit[si][sj] == 0: # 청소되지 않은 칸
        visit[si][sj] = cnt

    flag = 0

    if sd == 0:
        dir = dir_z
    elif sd == 1:
        dir = dir_f
    elif sd == 2:
        dir = dir_s
    elif sd == 3:
        dir = dir_t

    for di, dj, cd in dir: # 3 - 1반시계 방향으로 회전, 바라보는 방향
        ci, cj = si + di, sj + dj # 앞쪽칸
        if 0 <= ci < N and  0 <= cj < M and maps[ci][cj] != 1 and visit[ci][cj] == 0:
            flag = 1
            # 3 - 2
            clean(ci, cj, cd, cnt+1)
            if flag2 == 1:
                return
    # 2

    if flag == 0:
        # 2-1
        if sd == 0 and 0 <= si+1 < N and maps[si+1][sj] != 1:
            clean(si+1, sj, sd, cnt)
        elif sd == 1 and 0 <= sj-1 < M and maps[si][sj-1] != 1:
            clean(si, sj-1, sd, cnt)
        elif sd == 2 and 0 <= si-1 < N and maps[si-1][sj] != 1:
            clean(si-1, sj, sd, cnt)
        elif sd == 3 and 0 <= sj+1 < M and maps[si][sj+1] != 1:
            clean(si, sj+1, sd, cnt)
        else:
            # 2-2 : 모든 함수 자체를 다 끝내야 하기 때문.
            flag2 = 1

N, M = map(int, stdin.readline().split())
ni, nj, direction = map(int, stdin.readline().split()) # 0북 1동 2남 3서
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = 0
dir_z = [(0, -1, 3), (1, 0, 2), (0, 1, 1), (-1, 0, 0)]
dir_f = [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)]
dir_s = [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)]
dir_t = [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)]
flag2 = 0
clean(ni, nj, direction, 1)
print(ans)