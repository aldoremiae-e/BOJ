def solution(s, n):
    answer = 0
    i = 1
    while True:
        if (i * s) >= n:
            answer = i
            break
        i += 1
    
    return answer