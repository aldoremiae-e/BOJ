from collections import deque
N = int(input())
lst = deque([])
for _ in range(N):
    lst.append(int(input()))
lst = sorted(lst)
for l in lst:
    print(l)