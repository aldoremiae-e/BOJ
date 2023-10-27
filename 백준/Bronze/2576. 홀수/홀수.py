lst = []
ans1 = 0
for _ in range(7):
    a = int(input())
    if a % 2:
        lst.append(a)
        ans1 += a
lst.sort()
if not lst:
    print(-1)
else:
    print(ans1)
    print(lst[0])
