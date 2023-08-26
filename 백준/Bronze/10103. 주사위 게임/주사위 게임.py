N = int(input())
a, b = 100, 100
for _ in range(N):
    ca, cb = map(int, input().split())
    if ca > cb:
        b -= ca
    elif ca < cb :
        a -= cb
    else:
        continue
print(a)
print(b)