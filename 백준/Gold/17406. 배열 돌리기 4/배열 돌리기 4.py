from copy import deepcopy
def rotate(arr, i):
    new = deepcopy(arr)
    cr, cc, cs = orders[i][0], orders[i][1], orders[i][2]
    for i in range(cs, -1, -1):
        for k in range(1, 2 * i + 1):
            new[cr - i][cc - i + k] = arr[cr - i][cc - i + k - 1]
        for k in range(1, 2 * i + 1):
            new[cr - i + k][cc + i] = arr[cr - i + k - 1][cc + i]
        for k in range(1, 2 * i + 1):
            new[cr + i][cc + i - k] = arr[cr + i][cc + i - k + 1]
        for k in range(1, 2 * i + 1):
            new[cr + i - k][cc - i] = arr[cr + i - k + 1][cc - i]
    return new

def solve(cnt, maps):
    global visit, ans
    if cnt == K:
        for i in range(N):
            ans = min(ans, sum(maps[i]))
        return
    for i in range(K):
        if visit[i] == 1:
            continue
        visit[i] = 1
        # 회전해야함
        new = rotate(maps, i)
        solve(cnt+1, new)
        visit[i] = 0

N, M, K = map(int, input().split())
# 초기 배열
board = [list(map(int, input().split())) for _ in range(N)]
# 연산 방법
orders = []
for _ in range(K):
    r, c, s = map(int, input().split())
    orders.append((r-1, c-1, s))
# 연산 순서
visit = [0] * K
ans = 5001
solve(0, board)
print(ans)