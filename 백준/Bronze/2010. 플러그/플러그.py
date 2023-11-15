N = int(input())
a = 0
for i in range(N):
    if i == N-1:
        a += int(input())
    else:
        a += int(input()) - 1
print(a)