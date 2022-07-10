# deque 써보기
from collections import deque

def func(si, sj, sw, cnt):
    global t
    q = deque([])
    i, j = si, sj
    # 시작지점 q에 넣기
    q.append((i, j))
    # 2차원 방문 배열 - 방문했다면 1로 바꿀 것임
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    # 거리?
    distance = 0
    while q:
        distance += 1
        # 지나갈 수 있는 공간
        check = deque([])
        # 먹을 수 있는 물고기
        fish = []
        for x, y in q:
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = x + di, y + dj
                # 틀안에 있고, 방문하지 않응, 물고기가 상어무게보다 작으면 먹을 수 있는 물고기
                if (0 <= ni < N and 0 <= nj < N) and visited[ni][nj] == 0 and 0 < arr[ni][nj] < sw:
                    fish.append((ni, nj))
                # 틀안에 있고, 방문하지않고, 물고기랑 상어무게가 같거나 없을 때
                elif (0 <= ni < N and 0 <= nj < N) and visited[ni][nj] == 0 and (arr[ni][nj] == 0 or arr[ni][nj] == sw):
                    check.append((ni, nj))
                    visited[ni][nj] = 1
        # 먹을 수 있는 물고기
        if fish:
            fish.sort()
            i, j = fish[0]
            # 먹은 물고기 수
            cnt += 1
            # 시작점 변경
            arr[i][j] = arr[si][sj] = 0
            # 거리 +1만큼 시간 +1
            t += distance
            # 크기와 먹은물고기 수가 같으면 크기 +1
            if cnt == sw:
                cnt = 0
                sw += 1
            return func(i, j, sw, cnt)
        # 얘는 뭐지
        q = check
    return

N = int(input()) # N 공간의 크기
arr = [list(map(int, input().split())) for _ in range(N)]

t = 0 # 시간
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j   # 상어시작 위치
            break
sw = 2  # 상어의 크기
cnt = 0
func(si, sj, sw, cnt)
print(t)
