from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = [0] * 10000001
    for i in tangerine:
        cnt[i] += 1
    lst = []
    for i in cnt:
        if i != 0:
            lst.append(i)
    lst = sorted(lst, reverse = True)
    if lst[0] >= k:
        answer = 1
    else:
        i = 0
        while k > 0:
            # k 보다 크거나 같은 수가 있다면 result = 1
            k -= lst[i]
            answer += 1
            i += 1
    return answer