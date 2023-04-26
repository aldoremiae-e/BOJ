s = input()
if len(s) == 3:
    if s[1] == '0':
        print(int(s[2]) + 10)
    elif s[2] == '0':
        print(int(s[0]) + 10)
elif len(s) == 4:
    print(20)
else:
    print (int(s[0]) + int(s[1]))