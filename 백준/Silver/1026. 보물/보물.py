from sys import stdin
from collections import deque

N = int(stdin.readline())
A = deque(map(int, stdin.readline().split()))
B = deque(map(int, stdin.readline().split()))
A = sorted(A)
B = sorted(B, reverse=True)
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)
