from sys import stdin
N = int(stdin.readline())
cnt = 0
flag = 1
while N >= 0:
    if N % 5 == 0:
        cnt += (N // 5)
        print(cnt)
        flag = -1
        break
    N -= 3
    cnt += 1
if flag > 0:
    print(-1)