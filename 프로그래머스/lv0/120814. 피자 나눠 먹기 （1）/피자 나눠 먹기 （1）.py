def solution(n):
    m = n // 7
    answer = m
    if n > m * 7:
        answer += 1
    return answer