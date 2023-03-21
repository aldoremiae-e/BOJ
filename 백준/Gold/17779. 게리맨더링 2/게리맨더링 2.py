from collections import deque
N = int(input())
maps = [[0] * (N+1) for _ in range(N+1)]
ans = 0
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in range(N):
        maps[i][j+1] = lst[j]
        ans += lst[j]

def solve(x, y, d1, d2):
    global ans
    temp = [[0]*(N+1) for _ in range(N+1)] #edge를 적을 이차원배열
    temp[x][y] = 5
    for i in range(1, d1+1):
        temp[x+i][y-i] = 5
        temp[x+d2+i][y-i+d2] = 5
    for i in range(1, d2+1):
        temp[x+i][y+i] = 5
        temp[x+i+d1][y+i-d1] = 5

    # 1번선거구
    f = 0
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if temp[r][c] == 5:
                break
            else:
                f += maps[r][c]
    s = 0
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if temp[r][c] == 5:
                break
            else:
                s += maps[r][c]
    t = 0
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if temp[r][c] == 5:
                break
            else:
                t += maps[r][c]
    ft = 0
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if temp[r][c] == 5:
                break
            else:
                ft += maps[r][c]
    e = ans - (f + s + t + ft)
    max_num = max(f, s, t, ft, e)
    min_num = min(f, s, t, ft, e)
    return max_num - min_num
# x y d1 d2 설정
ret = int(1e9)
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 > N:
                    continue
                if 1 > y - d1:
                    continue
                if y + d2 > N:
                    continue
                ret = min(ret, solve(x, y, d1, d2))
print(ret)