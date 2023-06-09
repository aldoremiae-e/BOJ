from itertools import combinations
def find(a, b):
    ret = 0
    for i in zip(a, b):
        if i[0] != i[1]:
           ret += 1
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(str, input().split()))
    my_dic = {'ISTJ': 0, 'ISFJ': 0, 'INFJ': 0, 'INTJ': 0,
              'ISTP': 0, 'ISFP': 0, 'INFP': 0, 'INTP': 0,
              'ESTP': 0, 'ESFP': 0, 'ENFP': 0, 'ENTP': 0,
              'ESTJ': 0, 'ESFJ': 0, 'ENFJ': 0, 'ENTJ': 0}
    ans, flag = 100000, False
    for l in lst:
        my_dic[l] += 1
        if my_dic[l] >= 3:
            flag = True
            ans = 0
            break
    if flag:
        print(ans)
    else:
        combs = set(combinations(lst, 3))
        for comb in combs:
            ans = min(ans, find(comb[0], comb[1]) + find(comb[1], comb[2]) + find(comb[2], comb[0]))
        print(ans)