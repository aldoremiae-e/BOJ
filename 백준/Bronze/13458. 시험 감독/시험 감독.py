from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())
ans = N


for i in range(N):
    num = (A[i] - B)
    if num <= 0:
        continue
    elif num <= C:
        ans += 1
    else:
        if num % C > 0:
            ans += (num // C) + 1
        else:
            ans += (num // C)

print(ans)