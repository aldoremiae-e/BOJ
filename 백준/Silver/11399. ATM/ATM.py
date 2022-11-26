from sys import stdin
from collections import deque
N = int(stdin.readline().rstrip())
P = deque(map(int, stdin.readline().rstrip().split()))
P = sorted(P)
cnt = 0
for i in range(len(P)):
    P[i] = P[i] + cnt
    cnt = P[i]
print(sum(P))