from sys import stdin
N = int(stdin.readline())

stars = [[' '] * N for _ in range(N)]

def res(i, j, n):
    if n == 3:
        stars[i][j-1] = stars[i][j] = stars[i][j+1] = '*'
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        stars[i+2][j-1] = stars[i+2][j] = stars[i+2][j+1] = '*'
    else:
        n = n // 3
        res(i, j, n)
        res(i, j - n, n)
        res(i, j + n, n)
        res(i + n, j - n, n)
        res(i + n, j + n, n)
        res(i + 2*n, j, n)
        res(i + 2*n, j - n, n)
        res(i + 2*n, j + n, n)

res(0, N//2, N)
for i in stars:
    print(''.join(i))