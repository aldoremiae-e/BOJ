from heapq import heappop, heappush
# 다익스트라
def djikstra(start, visit, v):
    q = []
    q.append((0, start))
    # 시작노드 큐 모두 넣기
    visit[start] = 0
    '''
    for val_node in v[start]:
        heappush(q, val_node)
        # 초기 visit
        visit_pth[val_node[1]] = val_node[0]
    '''
    while q:
        cur_val, cur_node = heappop(q)
        # 이미 visit에 최소값이 있는 경우 패스
        # 개선된 다익스트라
        if visit[cur_node] < cur_val:
            continue
        # 현재 노드와 이어진 노드
        for val_node in v[cur_node]:
            val, node = val_node[0], val_node[1]
            if visit[node] > val + cur_val:
                # 최소값 찾으면 visit 업데이트
                visit[node] = val + cur_val
                # 큐에다가 넣어주자
                heappush(q, (val+cur_val, node))

    return visit
N, M, X = map(int, input().split())
v1 = [[]for _ in range(N)]
v2 = [[]for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    v1[a-1].append((c, b-1))
    v2[b-1].append((c, a-1))

inf = int(1e9)
visit_pth = [inf] * N
visit_pth2 = [inf] * N
# 파티장에서 집까지
visit_pth = djikstra(X-1, visit_pth, v1)
# 집에서 파티장까지
visit_pth2 = djikstra(X-1, visit_pth2, v2)
ans = 0
for a in zip(visit_pth, visit_pth2):
    ans = max(ans, (a[0] + a[1]))
print(ans)