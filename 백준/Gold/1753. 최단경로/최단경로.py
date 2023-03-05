from sys import stdin
from pprint import pprint
from heapq import heappush, heappop

def dijkstra(s):
    q = []
    heappush(q, (0, s))
    dis[s] = 0
    while q:
        dist, node = heappop(q) # 거리가 작은거 먼저뺌 2.(1-2, 2) 3.(1-3, 3)
        if dis[node] < dist: # 3이랑
            continue
        for next in maps[node]:
            weight, n = next[0], next[1] # 인접한 노드와 현재노드와 인접한 노드 사이 가중치
            val = dis[node] + weight # 시작~큐에서 뽑아낸 노드까지의 거리 + 큐에서 뽑아낸 노드와 그 노드와 인접한 노드 사이의 거리
            # 1. (1 - 2) 2. (1-2-3) < (1-3)
            if val < dis[n]: # 1. (1 -2) < (inf)
                dis[n] = val
                heappush(q, (val, n))
    return dis

# 입력
V, E = map(int, stdin.readline().split())
start = int(stdin.readline())
maps = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    maps[u].append((w, v))

visit = [False] * (V+1)
dis = [int(1e9)] * (V+1)

ans = dijkstra(start)

for i in range(1, V+1):
    if ans[i] == int(1e9):
        print('INF')
    else:
        print(ans[i])