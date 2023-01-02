from sys import stdin, maxsize
import heapq
INF = maxsize

def dijkstra(start):
    distance = [INF] * (N+1)
    heap = []
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        # 최소비용 뺄것
        cost, node = heapq.heappop(heap)
        for next_cost, next_node in graph[node]:
            next_cost = next_cost + cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, [next_cost, next_node])
    return distance

N, M, X = map(int, stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]

for i in range(M):
    s, e, t = map(int, stdin.readline().split())
    graph[s].append([t, e])

answer = [0] * (N+1)

for i in range(1, N+1):
    arr = dijkstra(i)
    answer[i] += arr[X]
    arr2 = dijkstra(X)
    answer[i] += arr2[i]
print(max(answer))