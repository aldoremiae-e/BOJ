from sys import stdin
from collections import deque
lst = deque([])
N = int(input())
for _ in range(N):
    lst.append(list(map(int, stdin.readline().split())))
lst = sorted(lst, key=lambda x:(x[0],x[1]))
for i in lst:
    print(i[0], i[1])