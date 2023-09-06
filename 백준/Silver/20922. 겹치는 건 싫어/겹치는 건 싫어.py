N, K = map(int, input().split())
lst = list(map(int,input().split()))

ans = 0
start, end = 0, 0
check = {}
while end < N:
    if lst[end] in check:
        if check[lst[end]] == K:
            check[lst[start]] -= 1
            start += 1
        else:
            check[lst[end]] += 1
            end += 1
            ans = max(ans, end - start)
    else:
        check[lst[end]] = 1
        end += 1
        ans = max(ans, end - start)
print(ans) 