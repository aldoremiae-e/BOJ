def solution(a, b):
    answer = 0
    i = 10000
    al, bl = 1, 1
    while i >= 10:
        if a % i == a:
            al = i
        if b % i == b:
            bl = i
        i //= 10
    c, d = a*bl + b, b*al + a
    answer = max(c, d)
    return answer