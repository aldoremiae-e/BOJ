from sys import stdin
lst = []
for i in range(10):
    N = int(stdin.readline())
    if (N % 42) not in lst:
        lst.append(N % 42)
print(len(lst))
