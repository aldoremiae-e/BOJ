from sys import stdin

N = int(stdin.readline())
S = []
for i in range(N):
    S.append(set(stdin.readline().split()))
cnt = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            cnt[i] += 1
print(max(cnt))