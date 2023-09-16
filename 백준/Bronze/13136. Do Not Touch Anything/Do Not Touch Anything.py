a,b,c = map(int,input().split())
a1 = a // c
b1 = b // c
if a % c > 0:
    a1 += 1
if b % c > 0:
    b1 += 1
print(a1 * b1)