from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline())
hq = []
for _ in range(N):
    x = int(stdin.readline())
    if x != 0:
        heappush(hq, (abs(x), x))
    else:
        if hq:
            q0, q1 = heappop(hq)
            print(q1)
        else:
            print(0)