from collections import Counter
xs = []
ys = []
ans = []
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
for key, val in Counter(xs).items():
    if val == 1:
        ans.append(key)
for key, val in Counter(ys).items():
    if val == 1:
        ans.append(key)
print(*ans)