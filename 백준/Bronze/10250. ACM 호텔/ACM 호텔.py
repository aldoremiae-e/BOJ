import sys
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    cnt = 1
    flag = 0
    for w in range(1, W+1):
        for h in range(1, H+1):
           if cnt == N:
               flag = 1
           if flag == 1:
               break
           cnt += 1
        if flag == 1:
            print('{}'.format(h), end='')
            print('{0:02d}'.format((w)))
            break

