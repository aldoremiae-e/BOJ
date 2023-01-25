from sys import stdin
N, M, B = map(int, stdin.readline().split())
arr = []
for _ in range(N):
    arr += list(map(int, stdin.readline().split()))
ans = int(1e9)
high = 0
for i in range(257):
    work1, work2 = 0, 0
    for k in arr:
        if k > i:
            work1 += (k - i)
        else:
            work2 += (i - k)
    if work2 > work1 + B:
        continue
    cnt = work1 * 2 + work2
    if cnt <= ans:
        ans = cnt
        high = i
print(ans, high)