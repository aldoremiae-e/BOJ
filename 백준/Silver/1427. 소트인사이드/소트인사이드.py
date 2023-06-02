N = input()
l = len(N)
N = int(N)
lst = []
d = 10 ** (l-1)
while d >= 1:
    n = N // d
    lst.append(n)
    N = N % d
    d //= 10
lst = sorted(lst, reverse=True)
for i in range(l):
    print(lst[i], end='')