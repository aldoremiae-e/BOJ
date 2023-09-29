N, K = map(int, input().split())
names = [[0,0,0,0]]
for _ in range(N):
    n, g, s, c = map(int, input().split())
    names.append([g, s, c, n])
names.sort(key=lambda x:(-x[0], -x[1], -x[2]))

memo = {names[0][3]: 1}
score = 1
for i in range(1, N+1):
    post = names[i-1]
    cur = names[i]
    for medal in range(3):
        if post[medal] > cur[medal]:
            score += 1
            memo[cur[3]] = score
            break
        else:
            continue
    if cur[3] not in memo:
        memo[cur[3]] = score
        score += 1
print(memo[K])