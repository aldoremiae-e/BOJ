from sys import stdin

N = int(stdin.readline())
real = list(map(int, stdin.readline().split()))
a = min(real)
b = max(real)
if N == 1: # 제곱수
    print(real[0] ** 2)
else:
    print(a * b)
    