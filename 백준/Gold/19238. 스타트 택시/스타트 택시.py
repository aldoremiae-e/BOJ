from collections import deque
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N, M, Oil = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ti, tj = map(int, input().split())
ti, tj = ti-1, tj-1

def dfs(si, sj):
    visit = [[0] * N for _ in range(N)]
    visit[si][sj] = 1
    q = deque()
    q.append((si, sj))
    while q:
        ni, nj = q.popleft()
        for di, dj in dir:
            ci, cj = ni + di, nj + dj
            if (0 <= ci < N and 0 <= cj < N) and visit[ci][cj] == 0 and maps[ci][cj] != 1:
                visit[ci][cj] = visit[ni][nj] + 1
                q.append((ci, cj))
    return visit
#people = deque()
s_maps = {} # s_maps[idx] : [(시작), (도착), 거리맵]
for i in range(1, M+1):
    ssi, ssj, eei, eej = map(int, input().split())
    vm = dfs(ssi-1, ssj-1)
    s_maps[i] = [(ssi-1, ssj-1), (eei-1, eej-1), vm]
#    people.append((ssi-1, ssj-1))
#people = sorted(people)
# 승객정하기
flag = 0
while 1:
    if s_maps:
        decide = deque()
        for key, val in s_maps.items():
            si, sj = val[0][0], val[0][1]
            ei, ej = val[1][0], val[1][1]
            ttp = val[2][ti][tj] - 1 # 택-승까지의 연료
            pta = val[2][ei][ej] - 1 # 승-도까지의 연료
            decide.append((ttp, (si, sj), pta, (ei, ej), key))
        decide = sorted(decide)
        taxi_to_pas = decide[0][0]
        pas_to_arr = decide[0][2]
        if taxi_to_pas < 0 or pas_to_arr < 0:
            flag = 1
            break # 승객 못태워 또는 도착못해
        if Oil <= taxi_to_pas:
            flag = 1
            break # 연료부족
        else:
            Oil -= taxi_to_pas
        if Oil < pas_to_arr:
            flag = 1
            break # 연료부족
        else:
            Oil += pas_to_arr  # 연료충전
            ti, tj = decide[0][3][0], decide[0][3][1]
            maps[ti][tj] = 0
            maps[decide[0][1][0]][decide[0][1][1]] = 0
            del s_maps[decide[0][4]]
    else:
        break
if flag == 1:
    print(-1)
else:
    print(Oil)