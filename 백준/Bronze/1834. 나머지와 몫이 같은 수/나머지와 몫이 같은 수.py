N = int(input())
cnt = 0
for i in range(1, N):
    cnt += (N * i) + i
print(cnt)