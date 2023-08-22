n = int(input())
a,b,c = map(int,input().split())
if a > n:
    a = n
if b > n:
    b = n
if c > n:
    c = n
print(a + b + c)