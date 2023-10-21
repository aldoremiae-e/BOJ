N = int(input())
n = N-1
for i in range(N):
    if i == 0:
        print(' '*(n) + '*')
    else:
        print(' '*(n-i) + '*' + ' '*(2*i-1)+'*')