T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    A = sorted(A)
    print(A[-3])