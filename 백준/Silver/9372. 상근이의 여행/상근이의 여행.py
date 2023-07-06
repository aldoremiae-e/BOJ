from collections import deque
def dfs(start, cnt):
    visit.append(start)
    for next in country[start]:
        if next not in visit:
            cnt = dfs(next, cnt+1)
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 그래프 구현
    country = {}
    first_c = 0
    for i in range(M):
        a, b = map(int, input().split())
        if first_c == 0:
            first_c = a
        if a not in country:
            country[a] = [b]
        else:
            country[a].append(b)
        if b not in country:
            country[b] = [a]
        else:
            country[b].append(a)
    # 간 나라의 수, 탄 비행기 종류
    # 모든 나라를 가야하니까 완전탐색
    visit = []
    ans = dfs(first_c, 0)
    print(ans)