from sys import stdin

X = int(stdin.readline())
lst = [64, 32, 16, 8, 4, 2, 1]
i = 0
cnt = 0
while X > 0:
    if X >= lst[i]:
        cnt += 1
        X -= lst[i]
    i += 1
    if X == 0:
        break
print(cnt)