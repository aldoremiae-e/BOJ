from heapq import heappush, heappop
def dijkstra(start):
    q = []
    q.append((0, start))
    ret = [inf] * (N+1)
    ret[start] = 0
    while q:
        cur_val, cur_node = heappop(q)
        # 개선된 다익스트라
        if ret[cur_node] < cur_val:
            continue
        for val, node in v[cur_node]:
            if ret[node] > val + cur_val:
                ret[node] = val + cur_val
                heappush(q, (val+cur_val, node))
    return ret
N, E = map(int, input().split())
v = [[] for _ in range(N+1)]
for _ in range(E):
    s, e, k = map(int, input().split())
    v[s].append((k, e))
    v[e].append((k, s))
p1, p2 = map(int, input().split())
inf = int(1e9)
ans = inf
ret1 = dijkstra(1)
ret2 = dijkstra(p1)
ret3 = dijkstra(p2)
ans = min(ans, ret1[p1] + ret2[p2] + ret3[N], ret1[p2] + ret3[p1] + ret2[N])
if ans >= inf:
    print(-1)
else:
    print(ans)