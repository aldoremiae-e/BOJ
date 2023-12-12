N, a, b, c, d = map(int, input().split())
board = [[0] * (2*N+1) for _ in range(2*N+1)]
board[N][N] = 1

ans = 0
def dfs(n, ci, cj, num):
    global board, ans
    if n == N:
        ans += num
        return
    if board[ci][cj+1] == 0:
        board[ci][cj+1] = 1
        dfs(n+1, ci, cj+1, num*(a/100))
        board[ci][cj + 1] = 0
    if board[ci][cj-1] == 0:
        board[ci][cj-1] = 1
        dfs(n+1, ci, cj-1, num*(b/100))
        board[ci][cj-1] = 0
    if board[ci-1][cj] == 0:
        board[ci-1][cj] = 1
        dfs(n+1, ci-1, cj, num*(c/100))
        board[ci-1][cj] = 0
    if board[ci+1][cj] == 0:
        board[ci+1][cj] = 1
        dfs(n+1, ci+1, cj, num*(d/100))
        board[ci+1][cj] = 0
dfs(0, N, N, 1)
print(ans)