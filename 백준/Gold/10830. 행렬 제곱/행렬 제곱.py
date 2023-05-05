def multi(A1, A2):
    new_A = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num = 0
            for k in range(n):
                num += A1[i][k] * A2[k][j]
            new_A[i][j] = num % 1000
    return new_A

def conquer(A, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] = A[i][j] % 1000
        return A
    tmp = conquer(A, b//2)
    if b % 2:
        return multi(multi(tmp, tmp), A)
    else:
        return multi(tmp, tmp)

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = conquer(arr, b)
for i in range(n):
    print(*res[i])