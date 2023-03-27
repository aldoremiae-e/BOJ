from collections import deque


# input
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수
maps = [[0] * N for _ in range(N)]
for _ in range(K): # 사과의 위치
    i, j = map(int, input().split())
    maps[i-1][j-1] = 1
L = int(input()) # 뱀 방향 변환 횟수
Llst = deque()
for _ in range(L):
    x, c = map(str, input().rstrip().split())
    x = int(x) # 시간 <= 10000
    Llst.append((x, c))

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = 1 #뱀의 길이
snake_q = deque()
snake_q.append((0, 0))
time = 0
flag = 0 # 게임시작

rot = 'D'
idx = 0
if Llst:
    if time == Llst[0][0]:
        f_time, f_rot = Llst.popleft()
        rot = f_rot
        if f_rot == 'D':
            idx = (idx + 1) % 4
        else:
            idx = (idx - 1) % 4

si, sj = 0, 0
while 1:
    if time > 10100: # 끝나지 않을 떄
        break
    time += 1
    di, dj = dir[idx][0], dir[idx][1]
    ci, cj = si + di, sj + dj # 머리칸
    # 머리가 벽, 자기자신의 몸과 부딪힐때
    if 0 <= ci < N and 0 <= cj < N:
        if (ci, cj) in snake_q:
            break
        else:
            # 게임진행
            if maps[ci][cj] == 1:
                maps[ci][cj] = 0
                si, sj = ci, cj
            else:
                si, sj = ci, cj
                snake_q.popleft()
            snake_q.append((ci, cj))
    else:
        # 벽과 부딪힐 때
        break
    # 시간이 끝나고 난 뒤
    if Llst:
        if time == Llst[0][0]:
            f_time, f_rot = Llst.popleft()
            rot = f_rot
            if f_rot == 'D':
                idx = (idx + 1) % 4
            else:
                idx = (idx - 1) % 4
print(time)