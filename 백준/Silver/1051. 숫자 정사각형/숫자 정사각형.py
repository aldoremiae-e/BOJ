from sys import stdin

N, M = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().strip())) for _ in range(N)]
l = min(N, M)
ans = 1
flag = 0
for k in range(l, 0, -1):
    if flag == 1:
        break
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            a = maps[i][j]
            b = maps[i][j+k-1]
            c = maps[i+k-1][j]
            d = maps[i+k-1][j+k-1]
            if a == b == c == d:
                if k ** 2 > ans:
                    ans = k ** 2
                    flag = 1
                    break
print(ans)