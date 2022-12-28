from sys import stdin
N = int(stdin.readline())
i = 1
cnt = 1
while 1:
    if N <= i:
        print(cnt)
        break
    i += (cnt * 6)
    cnt += 1