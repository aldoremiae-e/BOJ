from sys import stdin

N = int(stdin.readline())
lst = []
for _ in range(N):
    x, y = map(int, stdin.readline().split())
    lst.append((y, x))

lst = sorted(lst)
for i in lst:
    print(i[1], i[0])