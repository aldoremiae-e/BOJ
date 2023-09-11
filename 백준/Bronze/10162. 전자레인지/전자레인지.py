T = int(input())
# 300, 60, 10

a = T // 300
T -= (a * 300)
b = T // 60
T -= (b * 60)
c = T // 10
if T % 10:
    print(-1)
else:
    print(a, b, c)