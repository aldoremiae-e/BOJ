T = int(input())
for _ in range(T):
    N = int(input())
    uni = ''
    soju = -1
    for _ in range(N):
        s, l = map(str, input().split())
        if soju < int(l):
            soju = int(l)
            uni = s
    print(uni)