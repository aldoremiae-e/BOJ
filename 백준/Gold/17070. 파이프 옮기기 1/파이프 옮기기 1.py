N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dirs_lst = [(1, 11), (10, 11), (1, 10, 11)]
ans = 0
def find_dirs(si, sj, ei, ej):
    if ei - si == 0 and ej - sj == 1: # 가로
        dirs = dirs_lst[0]
    elif ei - si == 1 and ej - sj == 0: # 세로
        dirs = dirs_lst[1]
    elif ei - si == 1 and ej - sj == 1: # 대각선
        dirs = dirs_lst[2]
    return dirs

def solve(si, sj, ei, ej):
    global ans
    if ei == N-1 and ej == N-1:
        ans += 1
        return
    dirs = find_dirs(si, sj, ei, ej)
    for d in dirs:
        di, dj = d // 10, d % 10
        ni, nj = ei + di, ej + dj
        if (0 <= ni < N and 0 <= nj < N) and house[ni][nj] == 0:
            # 대각선일 때 빈칸이어야 하는 곳
            if di == 1 and dj == 1:
                if house[ni-1][nj] == 0 and house[ni][nj-1] == 0:
                    solve(ei, ej, ni, nj)
            else:
                solve(ei, ej, ni, nj)
if house[N-1][N-1] == 1:
    print(0)
else:
    solve(0, 0, 0, 1)
    print(ans)