L = int(input())
A = int(input()) # 국엉
B = int(input()) # 수학
C = int(input())
D = int(input())
ko, ma = 0 , 0
if A % C == 0:
    ko = A // C
else:
    ko = (A // C) + 1
if B % D == 0:
    ma = B // D
else:
    ma = (B // D) + 1
L -= max(ko, ma)
print(L)