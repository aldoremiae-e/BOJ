n = int(input())
cnt = 0
ret = 0
a = list(map(int,input().split()))
for i in range(n):
    if a[i] == 1:
        cnt += 1
        ret += cnt
    else:
        cnt = 0
print(ret)