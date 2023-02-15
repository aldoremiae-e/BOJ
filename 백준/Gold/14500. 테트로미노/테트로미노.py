from sys import stdin
N, M = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]
lst = [0] * 19
# 0
for i in range(N):
    for j in range(0, M-3):
        if lst[0] < maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i][j+3]:
            lst[0] = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i][j+3]
# 1
for j in range(M):
    for i in range(0, N-3):
        if lst[1] < maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+3][j]:
            lst[1] = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+3][j]

# 2,3,4,5,10,12,13,17
for i in range(0, N-2):
    for j in range(0, M-1):
        if lst[2] < maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+2][j+1]:
            lst[2] = maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 2][j + 1]
        if lst[3] < maps[i][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+2][j+1]:
            lst[3] = maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1]
        if lst[4] < maps[i][j] + maps[i][j+1] + maps[i+1][j] + maps[i+2][j]:
            lst[4] = maps[i][j] + maps[i][j + 1] + maps[i + 1][j] + maps[i + 2][j]
        if lst[5] < maps[i][j+1] + maps[i+1][j+1] + maps[i+2][j] + maps[i+2][j+1]:
            lst[5] = maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j] + maps[i + 2][j + 1]
        if lst[10] < maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j+1]:
            lst[10] = maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j + 1]
        if lst[12] < maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+1][j+1]:
            lst[12] = maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 1][j + 1]
        if lst[13] < maps[i+1][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+2][j+1]:
            lst[13] = maps[i + 1][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1]
        if lst[17] < maps[i][j+1] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j]:
            lst[17] = maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j]

# 6,7,8,9,11,14,15,18
for i in range(0, N-1):
    for j in range(0, M-2):
        if lst[6] < maps[i][j] + maps[i+1][j] + maps[i][j+1] + maps[i][j+2]:
            lst[6] = maps[i][j] + maps[i + 1][j] + maps[i][j + 1] + maps[i][j + 2]
        if lst[7] < maps[i][j+2] + maps[i+1][j] + maps[i+1][j+1] + maps[i+1][j+2]:
            lst[7] = maps[i][j + 2] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]
        if lst[8] < maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+2]:
            lst[8] = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 2]
        if lst[9] < maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+1][j+2]:
            lst[9] = maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]
        if lst[11] < maps[i][j+1] + maps[i][j+2] + maps[i+1][j] + maps[i+1][j+1]:
            lst[11] = maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j] + maps[i + 1][j + 1]
        if lst[14] < maps[i][j+1] + maps[i+1][j] + maps[i+1][j+1] + maps[i+1][j+2]:
            lst[14] = maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]
        if lst[15] < maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+1]:
            lst[15] = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 1]
        if lst[18] < maps[i][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+1][j+2]:
            lst[18] = maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 1][j + 2]

#16
for i in range(0, N-2):
    for j in range(0, M-2):
        if lst[16] < maps[i][j] + maps[i][j+1] + maps[i+1][j] + maps[i+1][j+1]:
            lst[16] = maps[i][j] + maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1]

print(max(lst))