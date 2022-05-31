T = int(input())
for _ in range(T):
    n = int(input()) # 13
    '''
    13/2 = 6 .. 1
    6/2 = 3 ... 0
    3/2 = 1 ... 1
    1/2 = 0 ... 1
    '''
    ans = []
    while(n/2 > 0):
        ans.append(n%2)
        n = n//2
    # print(ans)

    res = []
    for idx in range(len(ans)):
        if ans[idx] == 1:
           res.append(idx)
    for re in res:
        print(re, end=' ')