def solution(numer1, denom1, numer2, denom2):
    answer = []
    nu = numer1 * denom2 + numer2 * denom1
    de = denom1 * denom2
    N = max(nu, de)
    M = 1
    for i in range(1, N+1):
        if nu % i == 0 and de % i == 0:
            M = i
    answer = [nu//M, de//M]
    return answer