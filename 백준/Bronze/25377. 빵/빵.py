n = int(input())
small = 987654321
for i in range(n):
    a,b = map(int,input().split())
    if a > b:
        continue
    small = min(small, a)
if small == 987654321:
    print(-1)
else:
    print(small)