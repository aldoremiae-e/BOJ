def solution(ineq, eq, n, m):
    answer = 0
    if eq == '=':
        if ineq == '<':
            if n <= m:
                answer = 1
        else:
            if n >= m:
                answer = 1
    else:
        if ineq == '<':
            if n < m:
                answer = 1
        else:
            if n > m:
                answer = 1
    return answer