N = int(input())
arr = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())

def ref(ans, arr, i, pl, mi, mu, di, cnt):
    global maxnum, minnum
    if i == N:
        maxnum = ans if ans > maxnum else maxnum
        minnum = ans if ans < minnum else minnum
        return

    if pl > 0:
        #print(ans,cnt)
        ref(ans + arr[i], arr, i+1, pl-1, mi, mu, di, cnt+1)

    if mi > 0:
        #print(ans,cnt)
        ref(ans - arr[i], arr, i+1, pl, mi-1, mu, di, cnt+1)

    if mu > 0:
        #print(ans, cnt)
        ref(ans * arr[i], arr, i+1, pl, mi, mu-1, di, cnt+1)

    if di > 0:
        #print(ans, cnt)
        ref(ans // arr[i] if ans > 0 else -((-ans)//arr[i])
            , arr, i+1, pl, mi, mu, di-1, cnt+1)

ans = arr[0]
i = 1
maxnum = -999999999
minnum = 999999999
cnt = 0
ref(ans, arr, i, pl, mi, mu, di, cnt)
print(maxnum)
print(minnum)