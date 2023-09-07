from collections import deque
P = int(input())
for _ in range(P):
    q = deque(map(int, input().split()))
    tc = q.popleft()
    N = len(q)
    ans = 0
    for i in range(N-1, -1, -1):
        for j in range(i):
            if q[j] > q[j+1]:
                tmp = q[j]
                q[j] = q[j+1]
                q[j+1] = tmp
                ans += 1
    print(f'{tc} {ans}')