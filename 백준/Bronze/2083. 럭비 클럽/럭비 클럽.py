while 1:
    name, old, w = map(str, input().split())

    if name == "#":
        break
    if int(old) > 17 or int(w) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')