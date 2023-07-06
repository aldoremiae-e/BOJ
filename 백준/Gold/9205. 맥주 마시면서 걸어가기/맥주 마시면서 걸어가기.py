from collections import deque
def bfs():
    q = deque()
    q.append((sx, sy))
    visit = {}
    visit[(sx, sy)] = True
    while q:
        x, y = q.popleft()
        if abs(x - ex) + abs(y - ey) <= 1000:
            return True
        for store in corner_store:
            cx, cy = store[1],  store[2]
            if (cx, cy) in visit:
                continue
            if abs(cx-x) + abs(cy-y) > 1000:
                continue
            visit[(cx, cy)] = True
            q.append((cx, cy))
    return False
t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    corner_store = []
    for _ in range(n):
        cx, cy = map(int, input().split())
        d = abs(cx-sx) + abs(cy-sy)
        corner_store.append((d, cx, cy))
    ex, ey = map(int, input().split())
    ans = bfs()
    if ans:
        print('happy')
    else:
        print('sad')