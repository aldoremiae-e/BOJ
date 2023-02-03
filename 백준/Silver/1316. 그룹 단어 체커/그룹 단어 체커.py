from sys import stdin
N = int(stdin.readline())
cnt = 0
for _ in range(N):
    s = stdin.readline().rstrip()
    lst = []
    flag = 0
    for i in range(len(s)):
        if not lst:
            lst.append(s[i])
        if s[i] in lst:
            if s[i] == lst[-1]:
                continue
            else:
                flag = 1
                break
        else:
            lst.append(s[i])

    if flag == 0:
        cnt += 1
print(cnt)
