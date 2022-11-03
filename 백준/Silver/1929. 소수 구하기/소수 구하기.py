m, n = list(map(int, input().split()))
lst = [1 for _ in range(n+1)]
lst[0] = 0
lst[1] = 0

for i in range(2, n+1):
    if lst[i]:
        for j in range(i*i, n+1, i):
            lst[j] = 0
for k in range(m, n+1):
    if lst[k] == 1:
        print(k)
