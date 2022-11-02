from collections import deque
K, N = map(int, input().split())
lst = deque([])
mymax = 0
for _ in range(K):
    lst.append(int(input()))
mymax = sum(lst) // N
mymin = max(lst) // N
ans = (mymax+mymin) // 2
while mymin <= mymax:
    mid = (mymin + mymax) // 2
    if mid == 0:
        mid += 1
    cnt = 0
    for l in lst:
        cnt += (l // mid)
    if cnt >= N:
        ans = mid
        mymin = mid + 1
    else:
        mymax = mid - 1
print(ans)
