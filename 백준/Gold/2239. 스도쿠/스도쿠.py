N = 9
maps = [[0] * N for _ in range(9)]
zero = []
cnt = 0
for i in range(N):
    line = int(input())
    d = 100000000
    for j in range(N):
        maps[i][j] = line // d
        line = line % d
        if maps[i][j] == 0:
            zero.append((i, j))
            cnt += 1
        d //= 10
def check(si, sj, k):
    # k가 가로 세로 네모에 있는지 확인
    # 가로 - t세로
    for t in range(9):
        if maps[si][t] == k:
            return False
        if maps[t][sj] == k:
            return False
    # 네모
    ti, tj = (si // 3) * 3, (sj // 3) * 3
    for i in range(ti, ti+3):
        for j in range(tj, tj+3):
            if maps[i][j] == k:
                return False
    return True
flag = False
ret = [0] * 9
def dfs(count):
    global maps, flag
    if flag == True:
        return
    if count == cnt and flag == False:
        flag = True
        for i in maps:
            print(*i, sep="")
        return
    si, sj = zero[count]
    for k in range(1, 10):
        if check(si, sj, k):
            maps[si][sj] = k
            dfs(count + 1)
            maps[si][sj] = 0
    return
dfs(0)