from collections import deque
def bfs(sx, sy, ex, ey):
    global visit, maps
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = 1
    
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return visit[x][y] // 2
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in d:
            ci, cj = x + di, y + dj
            
            if (0 <= ci < 102 and 0 <= cj < 102) and maps[ci][cj] == 1 and visit[ci][cj] == 0:
                visit[ci][cj] = visit[x][y] + 1
                q.append((ci, cj))
                
            
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    global visit, maps
    answer = 0
    maps = [[0] * 102 for _ in range(102)]
    
    for xys in rectangle:
        x1, y1, x2, y2 = xys[0] * 2, xys[1] * 2, xys[2] * 2, xys[3] * 2
        
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    maps[x][y] = -1
                else:
                    if maps[x][y] == 0:
                        maps[x][y] = 1
    
    visit = [[0] * 102 for _ in range(102)]
    answer = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2)    
    return answer