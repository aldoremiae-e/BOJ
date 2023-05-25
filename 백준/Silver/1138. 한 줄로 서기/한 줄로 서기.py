N = int(input())
lst = [i for i in range(1, N+1)]
note = list(map(int, input().split()))
my_lst = []
for i in range(N):
    my_lst.append((lst[note[i]], i+1))
    lst.remove(lst[note[i]])
my_lst = sorted(my_lst)
for i in range(N):
    print(my_lst[i][1], end=' ')