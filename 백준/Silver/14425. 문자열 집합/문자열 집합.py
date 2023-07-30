N, M = map(int, input().split())
mydict = {}
for _ in range(N):
    s = input()
    mydict[s] = True
cnt = 0
for _ in range(M):
    target = input()
    if target in mydict:
        cnt += 1
print(cnt)