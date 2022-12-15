from sys import stdin

N = int(stdin.readline())
if (N % 4 == 0 and N % 100 != 0) or (N % 400 == 0):
    print(1)
else:
    print(0)