a = int(input())
b = (a // 2) + 1
if a % 2 == 0:
    print(b * b)
else:
    print(b * (b + 1))