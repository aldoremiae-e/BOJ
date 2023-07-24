T = int(input())
for _ in range(T):
    lst = list(map(str, input().split()))
    l = len(lst)
    ans = float(lst[0])
    for i in range(1, l):
        if lst[i] == '@':
            ans *= 3
        elif lst[i] == '%':
            ans += 5
        elif lst[i] == '#':
            ans -= 7
    print(f'{ans:.2f}')