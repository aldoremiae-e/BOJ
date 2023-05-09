def solution(n, control):
    answer = 0
    for c in control:
        if c == 'w':
            n += 1
        elif c == 's':
            n -= 1
        elif c == 'd':
            n += 10
        else:
            n -= 10
    return n