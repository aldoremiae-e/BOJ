from collections import deque
# 조합 MC3
def comb(m, k, arr): # O(2^m)
    global ans
    if k == 3:
        maps = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                maps[i][j] = arr[i][j]
        ans = max(ans, find_target(archers, maps))
        return
    for i in range(m, M):
        archers.append(i)
        comb(i+1, k+1, arr)
        archers.pop()

def bfs(start, maps): # O(3NM)
    global dead
    # 거리가 D이하인 적
    # 가장 가까운 적 (왼 오 위)
    dirs = [(0, -1),(-1, 0), (0, 1)]
    visit = [[0] * M for _ in range(N)]
    q = deque()
    q.append((N-1, start))
    visit[N-1][start] = 1
    while q:
        ci, cj = q.popleft()
        if maps[ci][cj] == 1:
            # 얘임
            dead.add((ci, cj))
            return
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if abs(N - ni) + abs(start - nj) > D:
                continue
            if visit[ni][nj] == 1:
                continue
            visit[ni][nj] = 1
            q.append((ni, nj))
    return
def check(maps):
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                return False
    return True
# 궁수공격
def find_target(archers, maps):
    global dead
    cnt = 0
    # 적이 다 사라질 때 까지
    while True:
        if check(maps):
            break
        dead = set()
        for j in archers:
            # 적 감지
            bfs(j, maps)
        # 공격
            # 감지된 적 3명을 0으로 처리
        cnt += len(dead)
        for dead_i, dead_j in dead:
            maps[dead_i][dead_j] = 0

        # 적은 한칸 아래로 이동.
        for j in range(M):
            for i in range(N - 1, -1, -1):
                if maps[i][j] == 1:
                    if i + 1 == N:
                        # 밖으로 나간 거
                        maps[i][j] = 0
                    else:
                        temp = maps[i][j]
                        maps[i][j] = 0
                        maps[i + 1][j] = 1
                else:
                    continue
    return cnt
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
archers = []
comb(0, 0, arr)
print(ans)