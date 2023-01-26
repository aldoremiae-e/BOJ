from sys import stdin

N, M = map(int, stdin.readline().split())
print(N // M)
print(N % M)