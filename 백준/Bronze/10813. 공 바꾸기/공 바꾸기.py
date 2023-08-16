N, M = map(int, input().split())
my_dict = {}
for i in range(1, N+1):
    my_dict[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    temp = my_dict[i]
    my_dict[i] = my_dict[j]
    my_dict[j] = temp

for key, value in my_dict.items():
    if key == N+1:
        print(value)
    else:
        print(value, end=' ')