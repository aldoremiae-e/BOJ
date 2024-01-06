import math
N = int(input())
start = int(input())
lst = []
for i in range(N-1):
    cur = int(input())
    lst.append(cur - start)
    start = cur
gcd = lst[0]
for i in range(1, len(lst)):
    gcd = math.gcd(gcd, lst[i])

ans = 0
for k in lst:
    ans += k // gcd - 1
print(ans)