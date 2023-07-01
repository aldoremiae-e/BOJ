N, M = map(int, input().split())
lst = [0] * N
for _ in range(M):
    i, j, k = map(int,input().split())
    i= i-1
    for t in range(i, j):
        lst[t] = k
print(*lst)