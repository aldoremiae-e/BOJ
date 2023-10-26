N = int(input())
lst = list(map(int, input().split()))
lst.sort()
tg1, tg2 = 0, 0
if lst[0] >= 0:
    tg1, tg2 = lst[0], lst[1]
elif lst[-1] <= 0:
    tg1, tg2 = lst[-2], lst[-1]
else:
    s, e = 0, N-1
    num = lst[s] + lst[e]
    tg1, tg2 = lst[s], lst[e]

    if num > 0:
        e -= 1
    elif num < 0:
        s += 1
        # 탐색
    num = abs(num)
    while s != e:
        cur = lst[s] + lst[e]
        if cur == 0:
            tg1, tg2 = lst[s], lst[e]
            break
        if num > abs(cur):
            tg1, tg2 = lst[s], lst[e]
            num = abs(cur)
        if cur > 0:
            e -= 1
        else:
            s += 1
print(tg1, tg2)