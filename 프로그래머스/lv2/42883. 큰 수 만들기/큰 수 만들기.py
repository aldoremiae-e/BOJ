def solution(number, k):
    answer = ''
    l = len(number)
    s, e = 0, k
    while e < l:
        maxnum = -1
        m_idx = 0
        for i in range(s, e+1):
            if maxnum < int(number[i]):
                maxnum = int(number[i])
                m_idx = i
                if maxnum == 9:
                    break
        s = m_idx + 1
        e += 1
        answer += str(maxnum)
    return answer