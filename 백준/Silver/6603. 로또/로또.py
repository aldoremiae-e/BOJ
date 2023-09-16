from itertools import combinations
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    else:
        k = lst[0]
    combs = list(combinations(lst[1:], 6))
    for comb in combs:
        print(*comb)
    print()