b1 = 2001
c1 = 2001
for _ in range(3):
    b2 = int(input())
    b1 = min(b2, b1)
for _ in range(2):
    c2 = int(input())
    c1 = min(c1, c2)
print(b1 + c1 - 50)