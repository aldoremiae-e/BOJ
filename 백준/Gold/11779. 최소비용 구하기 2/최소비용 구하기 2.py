import heapq
from sys import stdin

# 도시개수
n = int(stdin.readline())
# 버스개수
m = int(stdin.readline())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, v = map(int, stdin.readline().split())
    maps[i].append((j, v))
S, E = map(int, stdin.readline().split())
cost = [1e9] * (n+1)
visit = [[] for _ in range(n+1)]
def dijkstra(s, e):
    heap = []
    # 출발점, cost
    heapq.heappush(heap, (s, 0, [s]))
    cost[s] = 0
    while heap:
        cur, cst, vst = heapq.heappop(heap)
        if cost[cur] < cst:
            continue
        for end, val in maps[cur]:
            val += cst
            if val < cost[end]:
                cost[end] = val
                visit[end] = vst + [end]
                heapq.heappush(heap, (end, val, vst + [end]))

dijkstra(S, E)
print(cost[E])
print(len(visit[E]))
print(*visit[E])