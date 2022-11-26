from collections import deque
from sys import stdin

N = int(stdin.readline())
score = deque(map(int, stdin.readline().rstrip().split()))
M = max(score)
for i in range(N):
    score[i] = score[i]/M * 100
mean = sum(score)/N
print(mean)