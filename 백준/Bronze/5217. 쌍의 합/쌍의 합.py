T = int(input())
for _ in range(T):
    n = int(input())
    print('Pairs for %d:' %n, end=' ')
    s = 1
    for k in range((n-1)//2):
        if k != 0:
            print(',', end=' ')
        print(s, n-s, end='')
        s += 1
    print()
        