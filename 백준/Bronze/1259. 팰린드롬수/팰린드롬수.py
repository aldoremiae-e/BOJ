while 1:
    i = list(map(int, input()))
    if i[0] == 0:
        break
    else:
        if i == list(reversed(i)):
            print('yes')
        else:
            print('no')