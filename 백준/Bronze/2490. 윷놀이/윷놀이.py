for i in range (3):
    lst = list(map(int, input().split()))
    a = 0
    for j in lst:
        if j == 0:
            a += 1
            
    if a == 1:
        print('A')
    elif a == 2:
        print('B')
    elif a == 3:
        print('C')
    elif a == 4:
        print('D')
    else:
        print('E')