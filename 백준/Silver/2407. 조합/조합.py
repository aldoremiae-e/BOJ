from sys import stdin
n, m = map(int, stdin.readline().split())
bm = 1
idx = 1
bj = 1
'''
100 99 98 97 96 95 94
100-6=95
'''
for i in range(n, n-m, -1):
    bm *= i
    bj *= idx
    idx += 1

print(int(bm//bj))