c = input()
l = len(c)
s = ''
for i in range(l-1, -1, -1):
    s += c[i]
if s == c:
    print(1)
else:
    print(0)