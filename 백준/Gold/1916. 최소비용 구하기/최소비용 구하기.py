# 최소비용 구하기
import heapq
from sys import stdin

def dijkstra(S, E):
    global ans
    heap = []
    heapq.heappush(heap, [S, 0])
    visit[S] = 0
    while heap:
        cur, cost = heapq.heappop(heap)
        if visit[cur] < cost:
            continue
        for end, val in infos[cur]:
            # end까지 갈때까지의 비용
            val += cost
            if val < visit[end]:
                visit[end] = val
                heapq.heappush(heap, [end, val])

N = int(stdin.readline()) # 도시의 개수
M = int(stdin.readline()) # 버스의 개수
infos = [[] for _ in range(N+1)]
infos[0].append((0, 0))
for _ in range(M):
    # 출발번호 도착지번호 버스비용
    i, j, v = (map(int, stdin.readline().split()))
    infos[i].append((j, v))
# 출발 도착
s, e = map(int, stdin.readline().split())

visit = [1e9] * (N+1)
dijkstra(s, e)
print(visit[e])