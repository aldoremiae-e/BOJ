import math
from math import log2
def solution(s):
    answer = [0, 0]
    # 0지우기
    while True:
        def zero(s):
            q = ''
            for i in s:
                if i == '1':
                    q += '1'
                else:
                    answer[1] += 1
            return len(q)
        c = zero(s)
        # 이진법 만들기
        def bites(c):
            bite_len = int(log2(c)) + 1
            next_q = ''
            for i in range(bite_len-1, -1, -1):
                num = 2 ** i
                if c >= num:
                    next_q += '1'
                    c -= num
                else:
                    next_q += '0'
            return next_q
        s = bites(c)
        answer[0] += 1
        if s == '1':
            break
    return answer