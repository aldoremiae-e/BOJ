n = int(input())
N = 2
t = 1000000007
def square(A1, A2):
    Z = [[0, 0], [0, 0]]
    for i in range(N):
        for j in range(N):
            num = 0
            for k in range(N):
                num += A1[i][k] * A2[k][j]
            Z[i][j] = num % t
    return Z

def conquer(n, A):
    if n == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % t
        return A
    res = conquer(n//2, A)
    if n % 2:
        return square(square(res, res), A)
    else:
        return square(res, res)

arr = [[1, 1], [1, 0]]
fibo = conquer(n, arr)

print(fibo[1][0])