from collections import deque
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, input().split())
    lst = deque(list(map(int,input().split())))
    idx = deque([i for i in range(N)])
    ans = deque([])
    while lst:
        m = max(lst)
        if lst[0] < m:
            lst.append(lst.popleft())
            idx.append(idx.popleft())
        else:
            lst.popleft()
            ans.append(idx.popleft())
    for idx, val in enumerate(ans):
        if val == M:
            print(idx+1)