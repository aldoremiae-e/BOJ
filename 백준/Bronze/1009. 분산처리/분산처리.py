from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    lst = []
    i = 1
    while 1:
        if int(str(a ** i)[-1]) not in lst:
            lst.append(int(str(a**i)[-1]))
            i += 1
        else:
            break
    ans = lst[b % len(lst) - 1]
    if ans == 0:
        print(10)
    else:
        print(ans)