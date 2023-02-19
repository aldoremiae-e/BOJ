from sys import stdin

T, S = map(int, stdin.readline().split())

if (12 <= T < 17 and S == 0):
    print(320)
else:
    print(280)