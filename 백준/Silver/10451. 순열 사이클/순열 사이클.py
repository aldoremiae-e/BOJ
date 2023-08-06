T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    visit = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visit[i] == 1:
            continue
        visit[i] = 1
        def solve(start, goal):
            global cnt
            if start == goal:
                cnt += 1
                return
            visit[start] = 1
            solve(lst[start], goal)
        solve(lst[i], i)
    print(cnt)