K, N, M = map(int, input().split())

m = (K * N) - M
if m >= 0:
    print(m)
else:
    print(0)