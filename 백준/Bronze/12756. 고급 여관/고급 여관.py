a,b = map(int,input().split())
c,d = map(int,input().split())
x = d // a
y = b // c
if d % a != 0:
    x += 1
if b % c != 0:
    y += 1
if x > y:
    print("PLAYER B")
elif y > x:
    print("PLAYER A")
else:
    print("DRAW")