N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
    
lst.sort(reverse=True)
ans = -1
for i in range(N):
    ans = max(ans, lst[i] * (i+1))
print(ans)