#r(i) c(j) m d s
from collections import deque

# 파이어볼 이동
def solve():
    global q
    # 개수, 질량, 속도, 방향, 짝수, 홀수
    maps = [[[0, 0, 0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
    while q:
        sr, sc, sm, ss, sd = q.popleft()
        dr, dc = dir[sd][0], dir[sd][1]
        # 이동한 위치
        cr, cc = (sr + (dr * ss)) % N, (sc + (dc * ss)) % N
        maps[cr][cc][0] += 1 # 개수
        maps[cr][cc][1] += sm # 총질량
        maps[cr][cc][2] += ss # 총 속도
        maps[cr][cc][3] = sd # 마지막으로 들어온 칸의 방향
        if sd % 2 == 0:
            maps[cr][cc][4] += 1
        else:
            maps[cr][cc][5] += 1
    ret = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j][0] == 0:
                continue
            elif maps[i][j][0] == 1:
                ret += maps[i][j][1]
                q.append((i, j, maps[i][j][1], maps[i][j][2], maps[i][j][3]))
            else:
                m = maps[i][j][1] // 5
                s = maps[i][j][2] // maps[i][j][0]
                if m != 0:
                    ret += (m * 4)
                    # 방향
                    if maps[i][j][4] == maps[i][j][0] or maps[i][j][5] == maps[i][j][0]:
                        # 짝수
                        q.append((i, j, m, s, 0))
                        q.append((i, j, m, s, 2))
                        q.append((i, j, m, s, 4))
                        q.append((i, j, m, s, 6))
                    else:
                        q.append((i, j, m, s, 1))
                        q.append((i, j, m, s, 3))
                        q.append((i, j, m, s, 5))
                        q.append((i, j, m, s, 7))
    return ret

N, M, K = map(int, input().split())
# 방향
dir = [(N-1, 0), (N-1, 1), (0, 1), (1, 1), (1, 0), (1, N-1), (0, N-1), (N-1, N-1)]

q = deque()
for _ in range(M):
    fr, fc, fm, fs, fd = map(int, input().split())
    q.append((fr-1, fc-1, fm, fs, fd))
ans = 0
for _ in range(K):
    ans = solve()
print(ans)