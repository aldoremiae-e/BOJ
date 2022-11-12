import sys
from collections import deque
T = int(sys.stdin.readline())
def bfs(sx, sy):
    q = deque([])
    # 첫 단추
    if visited[sy][sx] == -1:
        return 0
    visited[sy][sx] = -1
    q.append((sx, sy))
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cnt = 0
    while q:
        cx, cy = q.popleft()
        for dx, dy in d:
           x, y = cx+dx, cy+dy
           if (0 <= x < M and 0 <= y < N) and arr[y][x] == 1 and visited[y][x] == 0:
               visited[y][x] = -1
               q.append((x, y))
        cnt += 1
    return 1

for tc in range(int(T)):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    arr = list([0 for _ in range(int(M))] for _ in range(N))
    visited = list([0 for _ in range(M)] for _ in range(N))
    lst = deque([])
    for i in range(K):
        # 배추의 위치
        x, y = map(int, sys.stdin.readline().split())
        lst.append((x, y))
        arr[y][x] = 1
    # 인접해있는 배추들한테는 지렁이가 한개임
    ans = 0
    for k in lst:
        ans += (bfs(k[0], k[1]))
    print(ans)