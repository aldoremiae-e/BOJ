from sys import stdin
N = int(stdin.readline())
skill = stdin.readline().rstrip()
cnt = 0
flagR = 0
flagK = 0
for i in skill:
    if i == 'L':
        flagR += 1
    elif i == 'R':
        if flagR > 0:
            cnt += 1
            flagR -= 1
        else:
            break
    elif i == 'S':
        flagK += 1
    elif i == 'K':
        if flagK > 0:
            cnt += 1
            flagK -= 1
        else:
            break
    else:
        cnt += 1
print(cnt)