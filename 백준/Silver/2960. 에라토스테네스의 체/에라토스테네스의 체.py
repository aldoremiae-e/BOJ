N, K = map(int, input().split())
my_dic = {}
k = 0
for i in range(2, N+1):
    if i in my_dic:
        continue
    for j in range(i, N+1, i):
        if j not in my_dic:
            my_dic[j] = True
            k += 1
        if k == K:
            print(j)
            exit()