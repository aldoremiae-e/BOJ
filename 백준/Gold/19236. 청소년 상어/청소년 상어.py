from copy import deepcopy
def fish_move(si, sj, Dic, Cmaps):
    # 상어 좌표 방향
    # 새로운 맵을 리턴
    # shark_move()에서 받은 lst
    # Dic은 딕셔너리
    Dic[0] = [-1, -1, -1]
    for key in range(1, 17):
        if key in Dic:
            ddd, ddi, ddj = Dic[key][0], Dic[key][1], Dic[key][2]
            # ni, nj
            for dir in range(0, 7):
                ni, nj = ddi + dirs[(ddd+dir) % 8][0], ddj + dirs[(ddd+dir) % 8][1]
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) != (si, sj):
                    target = Cmaps[ni][nj] #옮겨질 물고기
                    Cmaps[ni][nj] = Cmaps[ddi][ddj]
                    Cmaps[ddi][ddj] = target
                    Dic[key][0] = (ddd+dir) % 8
                    Dic[key][1] = ni
                    Dic[key][2] = nj
                    Dic[target][1] = ddi
                    Dic[target][2] = ddj
                    break
        else:
            continue
    return Cmaps, Dic

def shark_move(si, sj, sd, step, Cmaps, Dic):
    ci, cj = si + (dirs[sd][0] * step), sj + (dirs[sd][1] * step)
    if 0 <= ci < N and 0 <= cj < N and Cmaps[ci][cj] != 0:
        cd = Dic[Cmaps[ci][cj]][0]
        lst = [ci, cj, cd]
        return lst
    else:
        lst = [-1]
        return lst

def dfs(si, sj, sd, fishsum, Cmaps, Dic):
    global ans
    if(ans < fishsum):
        z = 0
    ans = max(ans, fishsum)

    for step in range(1, 4):
        mapcpy = deepcopy(Cmaps)
        diccpy = deepcopy(Dic)
        # 상어이동
        rlst = shark_move(si, sj, sd, step, mapcpy, diccpy)
        if rlst[0] == -1:
            continue
        else:
            ci, cj, cd = rlst[0], rlst[1], rlst[2]
            del diccpy[mapcpy[ci][cj]]
            plus = mapcpy[ci][cj]
            mapcpy[ci][cj] = 0
        # 물고기이동
        ret = fish_move(ci, cj, diccpy, mapcpy)

        dfs(ci, cj, cd, fishsum+plus, ret[0], ret[1])

dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
N = 4
maps = [[0] * 4 for _ in range(N)]
fish_dic = {}
# 입력
for i in range(4):
    input_lst = list(map(int, input().split()))
    for j in range(0, 8, 2):
        a, b = input_lst[j], input_lst[j+1]
        maps[i][j//2] = a
        fish_dic[a] = [b-1, i, j//2] # 방향 좌표
# 상어입장
shark_i, shark_j = 0, 0
ans = maps[0][0]
shark_d = fish_dic[maps[0][0]][0]
del fish_dic[maps[0][0]]
maps[0][0] = 0 # 빈공간
start = fish_move(shark_i, shark_j, fish_dic, maps)

# dfs
dfs(shark_i, shark_j, shark_d, ans, start[0], start[1])

# 출력
print(ans)