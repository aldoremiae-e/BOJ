N, M = map(int, input().split())
my_dict = {}
for i in range(1, N+1):
    my_dict[i] = i

for _ in range(M):
    a, b = map(int, input().split())
    s = []
    for key in range(a, b+1):
        s.append(my_dict[key])
    for key in range(a, b+1):
        n = s.pop()
        my_dict[key] = n
for key in range(1, N+1):
    print(my_dict[key], end=' ')