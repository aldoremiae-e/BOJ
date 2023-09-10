while True:
    s = int(input())
    if s == -1:
        break
    lst = []
    for i in range(1, s):
        if s % i == 0:
            lst.append(i)
    if sum(lst) == s:
        print(f'{s} =', end= ' ')
        for i in lst:
            print(i, end=' ')
            if i != lst[-1]:
                print("+", end=' ')
        print()
    else:
        print(f'{s} is NOT perfect.')