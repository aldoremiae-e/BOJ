from collections import deque
N, K = map(int, input().split())

arr = deque([(i+1) for i in range(N)])
ans = deque([])
while arr:
    for _ in range(K-1):
        arr.append(arr.popleft())
    ans.append(arr.popleft())
print('<', end='')
print(*ans,sep=', ', end='')
print('>')