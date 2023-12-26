n, a, b = map(int, input().split())
if n > b:
    print('Bus')
else:
    if a < b:
        print('Bus')
    elif a > b:
        print('Subway')
    else:
        print('Anything')