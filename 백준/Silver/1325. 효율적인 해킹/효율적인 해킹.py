from collections import deque

N, M = map(int, input().split())
comp = [[] for _ in range(N+1)]
for _ in range(M):
    val, key = map(int, input().split())
    comp[key].append(val)

def bfs(start):
    cnt = 1
    q = deque()
    q.append(start)
    visit = [False for _ in range(N+1)]
    visit[start] = True
    while q:
        cur = q.popleft()
        for j in comp[cur]:
            if not visit[j]:
                q.append(j)
                cnt += 1
                visit[j] = True
    return cnt

ans = []
max_num = 1
#  한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호
#  여러개면 오름차순
for i in range(1, N+1):
    cnt = bfs(i)
    if cnt > max_num:
        max_num = cnt
        ans.clear()
        ans.append(i)
    elif cnt == max_num:
        ans.append(i)

print(*ans)