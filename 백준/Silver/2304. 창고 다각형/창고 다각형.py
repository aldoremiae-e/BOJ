N = int(input())
arr = [0 for _ in range(1001)]
top_c, top_r = 0, 0
start, end = 1000, 0
for i in range(N):
    c, r = map(int, input().split())
    arr[c] = r
    if top_r < r:
        top_r = r
        top_c = c
    start = min(start, c)
    end = max(end, c)
ans = 0
height = 0
for i in range(start, top_c+1):
    if arr[i] == 0:
        ans += height
        continue
    height = max(arr[i], height)
    ans += height
height = 0
for i in range(end, top_c, -1):
    if arr[i] == 0:
        ans += height
        continue
    height = max(arr[i], height)
    ans += height
print(ans)