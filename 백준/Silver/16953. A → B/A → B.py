from sys import stdin
from collections import deque

A, B = map(int, stdin.readline().split())

def order1(num):
    return num*2
def order2(num):
    num = str(num) + '1'
    return int(num)

q = deque()
def bfs(start, cnt):
    q.append((start, cnt))
    while q:
        cur, curcnt = q.popleft()
        if cur == B:
            print(curcnt)
            return
        if order1(cur) <= B:
            q.append((order1(cur), curcnt + 1))
        if order2(cur) <= B:
            q.append((order2(cur), curcnt + 1))
    print(-1)
bfs(A, 1)