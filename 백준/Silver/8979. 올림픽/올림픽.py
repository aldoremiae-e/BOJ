N, K = map(int, input().split())
names = [[0,0,0,0]]
for _ in range(N):
    n, g, s, c = map(int, input().split())
    names.append([g, s, c, n])
names.sort(reverse=True)

score, same = 1, 0
if names[0][3] == K:
    print(score)
else:
    for i in range(1, N+1):
        post = names[i-1]
        cur = names[i]
        if post[:3] == cur[:3]:
            same += 1
        else:
            score += (same + 1)
            same = 0
        if cur[3] == K:
            print(score)
            break