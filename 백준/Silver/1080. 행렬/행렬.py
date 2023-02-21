from sys import stdin

N, M = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, stdin.readline().strip())) for _ in range(N)]

def chg(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            A[i][j] = 1 if A[i][j] == 0 else 0

ans = 0
flag = 0
for i in range(N-3+1):
    for j in range(M-3+1):
        if A[i][j] != B[i][j]:
            chg(i, j)
            ans += 1
        if A == B:
            flag = 1
            break
    if flag == 1:
        break
if flag == 1:
    print(ans)
else:
    if A == B:
        print(ans)
    else:
        print(-1)