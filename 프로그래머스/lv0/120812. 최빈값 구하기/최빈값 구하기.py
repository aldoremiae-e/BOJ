from collections import Counter
def solution(array):
    answer = 0
    c = Counter(array)
    max_num = max(list(c.values()))
    flag = False
    for key, val in c.items():
        if val == max_num:
            if flag:
                answer = -1
                break
            else:
                answer = key
                flag = True
    return answer