N = int(input())

memo = {}
memo[1] = 0
memo[2] = 1
memo[3] = 1
memo2 = {}
memo2[1] = 1
memo2[2] = 1
memo2[3] = 1
for i in range(4, N+1):
    if i not in memo:
        a, b, c = i-1, i-1, i-1
        if i % 2 == 0:
            a = memo[i//2]
        if i % 3 == 0:
            b = memo[i//3]
        c = memo[i-1]
        memo[i] = min(a, b, c) + 1
        if min(a, b, c) == a:
            memo2[i] = i//2
        elif min(a, b, c) == b:
            memo2[i] = i//3
        elif min(a, b, c) == c:
            memo2[i] = i-1
print(memo[N])
idx = N

while True:
    if idx == 1:
        print(memo2[1])
        break
    print(idx, end=' ')
    idx = memo2[idx]