from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
lst = deque()
cnt = 0

for i in range(N):
    money = int(stdin.readline())
    if money <= K:
        lst.append(money)
while K > 0:
    if (K - lst[-1]) >= 0:
        K = K - lst[-1]
        cnt += 1
    else:
        lst.pop()
    if K == 0:
        break
print(cnt)