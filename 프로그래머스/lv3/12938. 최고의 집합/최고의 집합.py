def solution(n, s):
    best = []
    max_num = 0
    if n > s:
        return [-1]
    for _ in range(n):
        best.append(s//n)
    idx = len(best) - 1
    for _ in range(s - sum(best)):
        best[idx] += 1
        idx -= 1
    return best
        