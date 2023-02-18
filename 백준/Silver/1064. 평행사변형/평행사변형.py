from sys import stdin

x1, y1, x2, y2, x3, y3 = map(int, stdin.readline().split())

slope1 = abs(y1-y2)/abs(x1-x2) if x1 != x2 else 1
slope2 = abs(y2-y3)/abs(x2-x3) if x2 != x3 else 1
slope3 = abs(y3-y1)/abs(x3-x1) if x3 != x1 else 1

if slope1 == slope2 == slope3:
    print(-1.0)
else:
    l1 = ((abs(x1-x2) ** 2) + (abs(y1-y2) ** 2)) ** 0.5 + ((abs(x3-x2) ** 2) + (abs(y3-y2) ** 2)) ** 0.5
    l2 = ((abs(x1-x2) ** 2) + (abs(y1-y2) ** 2)) ** 0.5 + ((abs(x3-x1) ** 2) + (abs(y3-y1) ** 2)) ** 0.5
    l3 = ((abs(x1-x3) ** 2) + (abs(y1-y3) ** 2)) ** 0.5 + ((abs(x3-x2) ** 2) + (abs(y3-y2) ** 2)) ** 0.5

    lm = max(l1, l2, l3) * 2
    ln = min(l1, l2, l3) * 2

    print(lm - ln)