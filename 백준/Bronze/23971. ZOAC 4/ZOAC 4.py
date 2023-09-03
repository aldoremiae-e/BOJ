H, W, N, M = map(int, input().split())

def solve(si, sj):
    cnt = 0
    for i in range(si, H, N+1):
        for j in range(sj, W, M+1):
            cnt += 1
    return cnt

ans = solve(0, 0)
print(ans)