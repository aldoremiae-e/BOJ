N = int(input())
lst = list(map(int, input().split()))
stack = [(lst[0], 1)]
ans = [0] * N
for i in range(1, N):
    top, idx = lst[i], i+1
    if stack[-1][0] < top:
        while stack and stack[-1][0] < top:
            stack.pop()
        if not stack:
            ans[i] = 0
        else:
            ans[i] = stack[-1][1]
    else:
        ans[i] = stack[-1][1]
    stack.append((top, idx))
print(*ans)