T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    k = int(a) - 1
    for i in range(len(b)):
        if i == k:
            continue
        print(b[i], end='')
    print()