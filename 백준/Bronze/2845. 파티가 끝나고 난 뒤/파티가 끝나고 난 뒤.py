L, P = map(int, input().split())
N = L * P
ans = []
maps = list(map(int, input().split()))
for i in range(5):
    ans.append(maps[i] - N)
print(*ans)