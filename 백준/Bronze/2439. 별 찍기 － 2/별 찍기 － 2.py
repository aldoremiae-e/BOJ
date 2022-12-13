from sys import stdin
N = int(stdin.readline())
for i in range(1, N+1):
    a = ' '
    b = '*'
    print(a * (N-i) + b * i)