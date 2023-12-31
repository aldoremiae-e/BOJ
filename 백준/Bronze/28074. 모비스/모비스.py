s = input()
cnt = 0
visit = [0,0,0,0,0]
for i in range(len(s)):
    if s[i] == 'M' and visit[0] != 1:
        visit[0] = 1
        cnt += 1
    elif s[i] == 'O' and visit[1] != 1:
        visit[1] = 1
        cnt += 1
    elif s[i] == 'B' and visit[2] != 1:
        visit[2] = 1
        cnt += 1
    elif s[i] == 'I' and visit[3] != 1:
        visit[3] = 1
        cnt += 1
    elif s[i] == 'S' and visit[4] != 1:
        visit[4] = 1
        cnt += 1
    if cnt == 5:
        break
if cnt == 5:
    print("YES")
else:
    print("NO")