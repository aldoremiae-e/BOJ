def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x-i):
            return 0
    return 1
def dfs(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):  # 열 순환
            col[x] = i  # [i, x]
            if check(x):    # 같은 행 / 대각선에 퀸이 있는지?
                dfs(x+1)

N = int(input())
ans = 0
col = [0] * N

dfs(0)
print(ans)