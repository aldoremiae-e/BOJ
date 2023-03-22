while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        ans = 'Yes' if a > b else 'No'
    print(ans)