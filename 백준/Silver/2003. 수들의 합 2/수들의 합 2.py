from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0] * N
arr_sum[0] = arr[0]
for k in range(1, N):
    arr_sum[k] = arr[k] + arr_sum[k-1]
arr_sum.insert(0, 0)
ans = 0
for i in range(N+1):
    for j in range(i, N+1):
        if arr_sum[j] - arr_sum[i] == M:
            ans += 1
print(ans)