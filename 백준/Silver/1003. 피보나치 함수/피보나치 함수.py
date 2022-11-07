import sys
T = int(sys.stdin.readline())
for tc in range(T):
    '''
     숫자 
        0  1 2 3
     0 | 1 0 1 1
     1 | 0 1 1 2
     3 = 2 1 = 1 0 1
    '''
    num = int(sys.stdin.readline())
    zerocnt = [1, 0]
    onecnt = [0, 1]
    if num > 1:
        for i in range(num-1):
            zerocnt.append(onecnt[-1])
            onecnt.append((zerocnt[-2]+onecnt[-1]))
    print(zerocnt[num], onecnt[num])