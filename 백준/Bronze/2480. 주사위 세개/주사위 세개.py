from sys import stdin

a, b, c = map(int, stdin.readline().split())
price = 0
if (a == b == c):
    price = 10000 + (1000 * a)
elif (a == b and b != c):
    price = 1000 + (100 * a)
elif (b == c and c != a):
    price = 1000 + (100 * b)
elif (c == a and a != b):
    price = 1000 + (100 * c)
else:
    price = max(a, b, c) * 100
print(price)