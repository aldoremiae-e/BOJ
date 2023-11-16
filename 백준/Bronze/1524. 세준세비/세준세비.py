T = int(input())
for _ in range(T):
    input()
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    while a and b:
        if a[-1] >= b[-1]:
            b.pop()
        else:
            a.pop()
    if a:
        print('S')
    elif b:
        print('B')
    else:
        print('C')