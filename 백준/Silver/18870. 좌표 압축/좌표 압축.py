from sys import stdin
from collections import deque
N = int(stdin.readline())
lst = deque(map(int, stdin.readline().split()))
dic = {val: idx for idx, val in enumerate(sorted(set(lst)))}

for i in lst:
  print(dic[i], end=' ')