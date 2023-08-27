loc = [0, 1, 2, 3]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    # a번컵 b번컵
    cur_a = loc.index(a)
    cur_b = loc.index(b)
    loc[cur_a] = b
    loc[cur_b] = a
print(loc[1])