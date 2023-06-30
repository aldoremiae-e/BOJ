N = int(input())
if N != 1:
    m = 2
    while N > 1:
        if N % m == 0:
            N = N // m
            print(m)
        else:
            m += 1
