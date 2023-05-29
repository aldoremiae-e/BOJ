while 1:
    a = input()
    if a == "END":
        break
    s = ""
    for i in range(len(a)):
        s += a[len(a) - i - 1]
    print(s)