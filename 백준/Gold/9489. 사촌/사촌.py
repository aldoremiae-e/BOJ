while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    lst = list(map(int, input().split()))
    dic1 = {lst[0]: 0} # 노드의 부모를 저장
    dic2 = {0: [lst[0]], lst[0]: []} # 노드의 자식을 저장

    p = 0
    idx = 1
    temp = []
    while idx < n:

        dic2[lst[idx]] = []
        if not temp:
            temp.append(lst[idx])
        else:
            if temp[-1] + 1 == lst[idx]:
                temp.append(lst[idx])
            else:
                dic2[lst[p]] = temp
                temp = [lst[idx]]
                p += 1
        dic1[lst[idx]] = lst[p]
        idx += 1
        if idx == n:
            dic2[lst[p]] = temp
    par = dic1[k]
    if par == 0:
        print(0)
    else:
        grand_par = dic1[par]
        total = 0
        for sibling in dic2[grand_par]:
            if sibling == dic1[k]:
                continue
            total += len(dic2[sibling])
        print(total)