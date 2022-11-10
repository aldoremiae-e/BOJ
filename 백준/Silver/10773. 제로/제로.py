import sys
from collections import deque
k = int(sys.stdin.readline())
lst = deque([])
for _ in range(k):
    n = int(sys.stdin.readline())
    if n != 0:
        lst.append(n)
    else:
        lst.pop()
print(sum(lst))