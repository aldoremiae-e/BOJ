from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    my_dic = {}
    for _ in range(n):
        name, typ = map(str, stdin.readline().split())
        if typ not in my_dic.keys():
            my_dic[typ] = 1
        else:
            my_dic[typ] += 1
    ans = 1
    for key, val in my_dic.items():
        ans *= (my_dic[key] + 1)
    print(ans - 1)