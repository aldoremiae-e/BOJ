from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    LCM = 0
    for i in range(1, M+1):
        if (i*N) % M == 0:
            LCM = (i*N)
            break
    xnums = []
    ynums = []
    while x <= LCM:
        xnums.append(x)
        x = x + M
    while y <= LCM:
        ynums.append(y)
        y = y + N
    C = set(xnums) & set(ynums)
    if not C:
        print(-1)
    else:
        print(*C)