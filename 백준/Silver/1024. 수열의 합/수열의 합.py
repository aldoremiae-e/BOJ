from sys import stdin

N, L = map(int, stdin.readline().split())

while True:
    flag = 0
    lst = [0] * L
    mid = N // L
    if L % 2 == 0:
        lst[L//2 - 1] = mid
    else:
        lst[L//2] = mid
    for i in range(L):
        if lst[i] != 0:
            continue
        else:
            if L % 2 == 0 and mid + (i - (L//2 - 1)) >= 0:
                lst[i] = mid + (i - (L//2 - 1))
            elif L % 2 and mid + (i - (L//2)) >= 0:
                lst[i] = mid + (i - (L//2))
        if i > 0 and lst[i] == 0:
            flag = 1
            break
    if flag == 1:
        print(-1)
        break
    if len(lst) > 100:
        print(-1)
        break
    elif sum(lst) == N:
        print(*lst)
        break
    else:
        L += 1
