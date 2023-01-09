from sys import stdin

N = int(stdin.readline())
lst = []
for i in range(N):
    w, h = map(int, stdin.readline().split())
    lst.append((w, h))
rank = []
for i in lst:
    cnt = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    rank.append(cnt)
print(*rank)