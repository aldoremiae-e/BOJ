def solution(ms, queries):
    answer = ''
    lst = []
    for i in range(len(ms)):
        lst.append(ms[i])
    for s, e in queries:
        ch_lst = []
        for k in range(e, s-1, -1):
            ch_lst.append(lst[k])
        lst[s:e+1] = ch_lst[:]
    for i in range(len(ms)):
        answer += lst[i]
    return answer