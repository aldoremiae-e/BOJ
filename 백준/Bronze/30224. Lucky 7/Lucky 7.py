n = input()
flag = 0
for i in range(len(n)):
    if n[i] == '7':
        flag = 1
        if int(n) % 7 == 0:
            print(3)
            break
        else:
            print(2)
            break
if flag == 0:
    if int(n) % 7 == 0:
        print(1)
    else:
        print(0)