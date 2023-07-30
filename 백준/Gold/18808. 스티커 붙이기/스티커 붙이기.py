from pprint import pprint
N, M, K = map(int, input().split())
maps = [[0] * M for _ in range(N)]

stickers = {}
def rotate(arr):
    NC, NR = len(arr[0]), len(arr)
    new_arr = [[0] * NR for _ in range(NC)]
    for j in range(NC):
        for i in range(NR-1, -1, -1):
            new_arr[j][NR-i-1] = arr[i][j]
    return new_arr
def check(si, sj, arr):
    r, c = len(arr), len(arr[0])
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                continue
            ni, nj = si + i, sj + j # 실제 맵에 들어갈 곳
            if not (0 <= ni < N and 0 <= nj < M):
                return False
            if maps[ni][nj] == 1:
                return False
    return True
def push(si, sj, arr):
    global maps
    r, c = len(arr), len(arr[0])
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                continue
            maps[si+i][sj+j] = arr[i][j]
for i in range(K):
    stickers[i] = []
for i in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers[i].append(sticker)
    for _ in range(3):
        sticker = rotate(sticker)
        stickers[i].append(sticker)

si, sj = 0, 0
idx = 0
while idx < K:
    flag = False
    for k in range(4):
        for si in range(N):
            for sj in range(M):
                if check(si, sj, stickers[idx][k]):
                    # 맵에 넣고
                    push(si, sj, stickers[idx][k])
                    idx += 1
                    # flag 바꿔서
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        idx += 1
ans = 0
for i in range(N):
    for j in range(M):
       if maps[i][j] == 1:
           ans += 1
print(ans)