from sys import stdin

N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
v = int(stdin.readline())
cnt = 0
for i in lst:
    if i == v:
       cnt += 1
print(cnt)