m = {'a':True, 'e':True, 'i':True, 'o':True, 'u':True}
s = {'b':True, 'c':True, 'd':True, 'f':True, 'g':True, 'h':True,
     'j':True, 'k':True, 'l':True, 'm':True, 'n':True, 'p':True,
     'r':True, 's':True, 't':True, 'v':True, 'w':True, 'x':True,
     'y':True, 'z':True}

# 같은글자 ee, oo는 가능
while True:
    pw = input()
    if pw == 'end':
        break
    flag = False
    # role 1
    for i in pw:
        if i in m:
            flag = True
            break
    if flag:
        # role 2
        a, b, c = 0, 0, pw[0]
        for k in range(len(pw)):
            if pw[k] in m:
                a += 1
                b = 0
            else:
                b += 1
                a = 0
            if a >= 3 or b >= 3:
                flag = False
                break
            if k > 0:
                # role 3
                if pw[k] == c:
                    if pw[k] == 'e' or pw[k] == 'o':
                        continue
                    else:
                        flag = False
                        break
                else:
                    c = pw[k]

    if flag:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')