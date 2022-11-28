from sys import stdin
from collections import deque
n = int(stdin.readline())
m = stdin.readline().rstrip()
lst = deque()
for i in m:
    lst.append(int(i))
print(sum(lst))