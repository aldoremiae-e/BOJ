N = int(input())
lst = [0] * (N+2)
for i in range(1, N+1):
    lst[i] = max(lst[i], lst[i-1])
    t, p = map(int, input().split())
    if i+t < N+2:
        lst[i+t] = max(lst[i] + p, lst[i+t])
print(max(lst[N], lst[N+1]))