n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in lst:
    if i == n:
        ans += 1
print(ans)