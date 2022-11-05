N, K = map(int, input().split())
ans = N
if K == 0:
    ans = 1
for _ in range(K-1):
    N -= 1
    ans *= N
while K > 0:
    ans /= K
    K -= 1
print(int(ans))