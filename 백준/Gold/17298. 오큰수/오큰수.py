N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N
stack = []
idx = N-1
while lst:
    cur = lst.pop()
    while stack and stack[-1] <= cur:
        stack.pop()
    if not stack:
        ans[idx] = -1
    else:
        ans[idx] = stack[-1]
    idx -= 1
    stack.append(cur)
print(*ans)