def solution(a, b):
    answer = 0
    al, bl = 0, 0
    i = 10000
    while i >= 10:
        if a % i == a:
            al = i
        if b % i == b:
            bl = i
        i //= 10
    answer = max((a * bl + b), 2 * a * b)
    return answer