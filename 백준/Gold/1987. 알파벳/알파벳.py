import sys
input = sys.stdin.readline
def dfs(si, sj, n):
    global ans, visit_alpha
    for di, dj in dirs:
        ci, cj = si + di, sj + dj
        if (ci < 0 or R <= ci) or (cj < 0 or C <= cj) or visit_alpha[maps[ci][cj]]:
            continue
        # 범위 안에 들고, 방문하지 않았고, 갔던 알파벳이 아님
        m = maps[ci][cj]
        visit_alpha[m] = True
        ans = max(n+1, ans)
        dfs(ci, cj, n+1)
        visit_alpha[m] = False


R, C = map(int, input().split())
maps = [[0] * C for _ in range(R)]
for i in range(R):
    s = input()
    for j in range(C):
        # int임
        maps[i][j] = ord(s[j]) - 65
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

visit_alpha = [False] * 26
visit_alpha[maps[0][0]] = True

ans = 1
dfs(0, 0, 1)
print(ans)