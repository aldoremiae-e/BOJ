from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
heap = []
for _ in range(N):
    x = int(stdin.readline())
    if x > 0:
        heappush(heap, -x)
    elif x == 0:
        if heap:
            num = heappop(heap)
            print(-num)
        else:
            print('0')