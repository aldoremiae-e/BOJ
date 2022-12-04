from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}
for _ in range(N):
    key, value = map(str, stdin.readline().split())
    dic[key] = value
for _ in range(M):
    find = stdin.readline().rstrip()
    print(dic[find])