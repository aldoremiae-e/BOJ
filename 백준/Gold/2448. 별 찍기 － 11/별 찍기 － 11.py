from sys import stdin
N = int(stdin.readline()) # 3 6 12 24 .. 3*2^^k

stars =[[' '] * (2 * N - 1) for _ in range(N)]

def res(i, j, n):
    if n == 3:
        # 정복
        # 1행
        stars[i][j] = '*'
        # 2행
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        # 3행
        for k in range(-2, 3):
            stars[i+2][j+k] = '*'
    else:
        # 분할
        n = n // 2
        res(i, j, n)
        res(i + n, j - n, n)
        res(i + n, j + n, n)
res(0, N-1, N)
for i in stars:
    print(''.join(i))