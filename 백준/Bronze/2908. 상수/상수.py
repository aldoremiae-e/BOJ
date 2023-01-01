from sys import stdin

A, B = stdin.readline().split()
rA, rB = '', ''
for i in reversed(A):
    rA += i
for i in  reversed(B):
    rB += i
if int(rA) > int(rB):
    print(rA)
else:
    print(rB)