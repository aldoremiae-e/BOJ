import sys
from collections import deque
N = int(input())
lst = deque([])
for i in range(N):
    lst.append(sys.stdin.readline().rstrip().split())
lst = sorted(lst, key= lambda x:int(x[0]))

for l in lst:
    print(l[0], l[1])