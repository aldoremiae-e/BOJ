z=int(input())
x=int(input())
if z % 2 == 1:
    y = z // 2 + x // 2 + 1
else:
    y = z // 2 + x // 2
print(y)
print(y-x)