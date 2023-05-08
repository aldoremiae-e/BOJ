T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start_in, end_in = -1, -1
        if ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5 <= r:
            start_in = 1
        if ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5 <= r:
            end_in = 1

        if start_in * end_in < 0:
            cnt += 1
    print(cnt)