import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
    global sum_num
    visit = [inf] * N
    visit[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        cur_val, cur_node = heappop(heap)
        for next_node, val in maps[cur_node]:
            if visit[next_node] > val + cur_val:
                visit[next_node] = val + cur_val
                heappush(heap, (val + cur_val, next_node))
    for i in range(N):
        if visit[i] <= M:
            sum_num += items[i]
    return
N, M, R = map(int, input().split())
items = list(map(int, input().split()))
inf = int(1e9)
maps = [[] for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().split())
    maps[a-1].append((b-1, l))
    maps[b-1].append((a-1, l))

maxnum = 0
for i in range(N):
    sum_num = 0
    dijkstra(i)
    maxnum = max(maxnum, sum_num)
print(maxnum)