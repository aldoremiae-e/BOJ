def solution(x1, x2, x3, x4):
    answer = True
    a1 = True if (x1 or x2) else False
    a2 = True if (x3 or x4) else False
    answer = True if (a1 and a2) else False
    return answer