N = int(input())
lst = []
for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b and b == c and c == a:
        lst.append(10000 + 1000*a)
    elif a == b and b != c:
        lst.append(1000 + 100*a)
    elif b == c and c != a:
        lst.append(1000 + 100*b)
    elif c == a and a != b:
        lst.append(1000 + 100*c)
    else:
        lst.append(100 * max(a, b, c))
print(max(lst))