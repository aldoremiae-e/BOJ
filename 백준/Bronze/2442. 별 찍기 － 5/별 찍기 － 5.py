N = int(input())
m = N-1
for i in range(N):
    # 0, 1, 2, 3 ,4 => 1 3 5 7 9
    star = (2*i + 1)
    print(' ' * m, '*' * star, sep='')
    m -= 1