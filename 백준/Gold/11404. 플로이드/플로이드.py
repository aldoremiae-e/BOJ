# 11404 플로이드 : 플로이드-워셜 중간지점을 거쳐서 찾는 최단경로

n = int(input())
m = int(input())
inf = int(1e9)
maps = [[inf] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        maps[i][j] = 0 if i == j else inf

for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a-1][b-1] = min(c, maps[a-1][b-1])

for mid in range(n):
    for i in range(n):
        for j in range(n):
            maps[i][j] = min(maps[i][j], maps[i][mid] + maps[mid][j])

for i in range(n):
    for j in range(n):
        if maps[i][j] == inf:
            print(0, end=' ')
        else:
            print(maps[i][j], end=' ')
    print()