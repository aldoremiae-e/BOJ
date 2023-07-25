from heapq import heappop, heappush
N, M, k = map(int, input().split())
maps = [[0] * N for _ in range(N)]
heap = []
# 상어의 위치 -> dict
shark_ij = {}
for i in range(N):
    input_lst = list(map(int, input().split()))
    for j in range(N):
        n = input_lst[j]
        if n != 0:
            maps[i][j] = n * 1000 + k
            shark_ij[n] = (i, j)
# 상어의 방향 ->list
shark_dir = list(map(int, input().split()))
for i in range(1, M+1):
    heappush(heap, (i, shark_dir[i-1]-1, shark_ij[i][0], shark_ij[i][1]))

# 상어의 우선순위 -> dict{n:[방향우선순위]}
shark_dict = {}
for i in range(1, M+1):
    shark_dict[i] = [[] for _ in range(4)]
    for j in range(4):
        shark_dict[i][j] = list(map(int, input().split()))
def next_heap(heap):
    nq = []
    while heap:
        # 번호, 방향, 좌표
        sn, sd, si, sj = heappop(heap)
        # 방향 우선순위
        dirs = shark_dict[sn][sd]
        # 다음방향이 될 것
        next_d = -1
        next_i, next_j = -1, -1
        flag = False
        for idx in range(4):
            if flag:
                break
            if dirs[idx] == 1:
                ni, nj = si - 1, sj
            elif dirs[idx] == 2:
                ni, nj = si + 1, sj
            elif dirs[idx] == 3:
                ni, nj = si, sj - 1
            elif dirs[idx] == 4:
                ni, nj = si, sj + 1

            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if maps[ni][nj] == 0:
                flag = True
                next_d, next_i, next_j = dirs[idx]-1, ni, nj
        #        heappush(next_ij, (0, idx, ni, nj))
            elif maps[ni][nj] // 1000 == maps[si][sj] // 1000:
                if next_d == -1:
                    next_d, next_i, next_j = dirs[idx]-1, ni, nj
        #        heappush(next_ij, (1, idx, ni, nj))
        #next_d, next_i, next_j = dirs[next_ij[0][1]] - 1, next_ij[0][2], next_ij[0][3]
        #nq.append((sn, next_d, next_i, next_j))
        nq.append((sn, next_d, next_i, next_j))
    return nq

time = 1
while time < 1001:
    heap = next_heap(heap)
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                continue
            maps[i][j] -= 1
            if maps[i][j] % 1000 == 0:
                maps[i][j] = 0
    nq = []
    while heap:
        n, d, i, j = heappop(heap)
        # 빈곳이거나, 자기냄새있는 곳으로 갔을 때
        if maps[i][j] == 0 or maps[i][j] // 1000 == n:
            maps[i][j] = n * 1000 + k
            nq.append((n, d, i, j))
    if len(nq) == 1:
        break
    else:
        heap = nq
        time += 1
if time < 1001:
    print(time)
else:
    print(-1)