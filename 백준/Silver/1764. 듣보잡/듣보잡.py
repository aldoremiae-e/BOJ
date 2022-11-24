from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())
'''
set : 중복을 허용하지 않고, 순서가 없다
set : O(1) , 교집합 &, 합집합 |, 차집합 - 다된다.
list : O(n)
'''
d = set()
b = set()
for _ in range(N):
  d.add(stdin.readline().rstrip())
for _ in range(M):
  b.add(stdin.readline().rstrip())

result = sorted(list(d & b))

print(len(result))
for i in result:
  print(i)
