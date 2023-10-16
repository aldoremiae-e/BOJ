N = int(input())
lst = list(map(int, input().split()))

F = {}
for i in range(N):
    if lst[i] not in F:
        F[lst[i]] = 0
    F[lst[i]] += 1

ans = [-1] * N
stack = [(lst[0], 0)]
for i in range(1, N):
    if F[stack[-1][0]] < F[lst[i]]:
        while stack and F[stack[-1][0]] < F[lst[i]]:
            num, idx = stack.pop()
            ans[idx] = lst[i]
    stack.append((lst[i], i))
print(*ans)