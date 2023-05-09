from collections import Counter
def solution(a, b, c, d):
    answer = 1
    lst = [a, b, c, d]
    C = Counter(lst)
    l = len(C)
    if l == 1:
        # 모두 같을 때
        answer = a * 1111
    elif l == 2:
        # 3:1 / 2:2
        a, b, flag_two = 0, 0, False
        for key, val in C.items():
            if val == 3:
                a = 10 * key
            elif val == 1:
                b = key
            else:
                flag_two = True
                if a == 0:
                    a = key
                else:
                    b = key
        if flag_two:
            answer = (a + b) * abs(b - a)
        else:
            answer = (a + b) ** 2
    elif l == 3:
        # 2 1 1
        for key, val in C.items():
            if val == 1:
                answer *= key 
    else:
        # 모두 다를 때
        answer = min(a, b, c, d)
    return answer