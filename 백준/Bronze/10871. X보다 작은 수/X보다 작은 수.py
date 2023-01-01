from sys import stdin
N, X = map(int, stdin.readline().split())
A = map(int, stdin.readline().split())
B = []
for i in A:
    if i < X:
        B.append(i)
print(*B)