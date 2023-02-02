from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
string = stdin.readline().rstrip()

P = ['IOI'] * N
for i in range(1, N):
    P[i] = P[i-1] + 'OI'
cnt = 0
L = len(P[N-1])
for i in range(M-L+1):
    if string[i:i + L] == P[N-1]:
        cnt += 1
print(cnt)