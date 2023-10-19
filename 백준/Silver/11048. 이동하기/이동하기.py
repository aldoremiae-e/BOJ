N, M = map(int, input().split())
lst = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    a = list(map(int, input().split()))
    for j in range(1, M+1):
        lst[i][j] = max(lst[i-1][j], lst[i][j-1]) + a[j-1]
print(lst[N][M])