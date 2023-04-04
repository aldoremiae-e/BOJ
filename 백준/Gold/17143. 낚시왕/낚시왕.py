def shark_move():
    global sharks_info
    new_maps = [[0] * C for _ in range(R)]
    for i in range(1, M+1):
        # 없는 상어는 보지않음
        if sharks_info[i] == []:
            continue
        # (현재위치) 속력 방향 크기
        si, sj, ss, sd, sz = sharks_info[i][0], sharks_info[i][1], sharks_info[i][2], sharks_info[i][3], sharks_info[i][4]

        if sd == 0 or sd == 1:
            ci, cj, cd = si, sj, sd
            for _ in range(ss):
                if ci == R-1:
                    cd = 0
                elif ci == 0:
                    cd = 1
                di, dj = dirs[cd][0], dirs[cd][1]
                ci += di
                cj += dj
                if ci == R-1:
                    cd = 0
                elif ci == 0:
                    cd = 1
            sharks_info[i] = [ci, cj, ss, cd, sz]

        if sd == 2 or sd == 3:
            ci, cj, cd = si, sj, sd
            for _ in range(ss):
                if cj == C-1:
                    cd = 3
                elif cj == 0:
                    cd = 2
                di, dj = dirs[cd][0], dirs[cd][1]
                ci += di
                cj += dj
                if cj == C-1:
                    cd = 3
                elif cj == 0:
                    cd = 2
            sharks_info[i] = [ci, cj, ss, cd, sz]

        ssi, ssj, sss, ssd, ssz = sharks_info[i][0], sharks_info[i][1], sharks_info[i][2], sharks_info[i][3], sharks_info[i][4]
        if new_maps[ssi][ssj] == 0:
            new_maps[ssi][ssj] = i
        else:
            temp_idx = new_maps[ssi][ssj]
            temp_size = sharks_info[temp_idx][4]
            if temp_size < ssz:
                new_maps[ssi][ssj] = i
                sharks_info[temp_idx] = []
            else:
                sharks_info[i] = []

    return new_maps
R, C, M = map(int, input().split())
sharks_info = {}
maps = [[0] * C for _ in range(R)]
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    # 세로 가로 속력 방향 크기
    # d 0 1 / 2 3 ㅗ ㅜ / ㅏ ㅓ
    sharks_info[i] = [r-1, c-1, s, d-1, z]
    maps[r-1][c-1] = i
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ans = 0

# 낚시왕 이동
for j in range(C):
    # 낚시
    for i in range(R):
        if maps[i][j] != 0:
            # 합
            ans += sharks_info[maps[i][j]][4]
            # 상어 정보 삭제, 맵에서 상어 삭제
            sharks_info[maps[i][j]] = []
            maps[i][j] = 0
            break
    # 상어이동 된 맵
    maps = shark_move()
print(ans)