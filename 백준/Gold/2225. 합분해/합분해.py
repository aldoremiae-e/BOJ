from sys import stdin
from pprint import pprint
N, K = map(int, stdin.readline().split())

maps = [[0] * (N+1) for _ in range(K+1)]

for i in range(1, K+1):
    maps[i][0] = 1
    for j in range(1, N+1):
        maps[i][j] = int((maps[i-1][j] + maps[i][j-1]) % 1e9)
#pprint(maps)
print(maps[K][N])