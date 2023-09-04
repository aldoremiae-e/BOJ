while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    max_num = max(a, b, c)
    flag = True
    if max_num == a:
        if a >= (b + c):
            print('Invalid')
            continue
    elif max_num == b:
        if b >= (a + c):
            print('Invalid')
            continue
    else:
        if c >= (a + b):
            print('Invalid')
            continue
    if a == b and b == c and c == a:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')