from collections import deque
N = int(input())
lst = list(map(int, input().split()))
q = deque([])
ans = [0 for _ in range(N)]
for i in range(N-1, -1, -1):
    if q:
        while q:
            if lst[i] < q[0]:
                ans[i] = q[0]
                break
            else:
                q.popleft()
                ans[i] = -1
        q.appendleft(lst[i])
    else:
        q.appendleft(lst[i])
        ans[i] = -1
print(*ans)