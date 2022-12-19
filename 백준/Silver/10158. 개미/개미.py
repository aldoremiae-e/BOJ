from sys import stdin
# 가로 w 세로 h, 좌표(p, q) => 45도 방향으로 (p+1, q+1)

w, h = map(int, stdin.readline().split())
p, q = map(int, stdin.readline().split())
t = int(stdin.readline())

if ((p + t) // w) % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if ((q + t) // h) % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)