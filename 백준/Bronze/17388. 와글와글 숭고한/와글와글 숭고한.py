a,b,c = map(int,input().split())
if a + b + c >= 100:
    print("OK")
else:
    if a > b:
        if b > c:
            print("Hanyang")
        else:
            print("Korea")
    else:
        if a > c:
            print("Hanyang")
        else:
            print("Soongsil")