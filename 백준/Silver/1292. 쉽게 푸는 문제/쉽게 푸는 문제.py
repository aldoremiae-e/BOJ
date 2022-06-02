lst = [i for i in range(1000) for j in range(i)]
N, M = map(int, input().split())
sumv = 0
for k in range(len(lst)):
    if N <= k+1 <= M:
        sumv += lst[k]
print(sumv)