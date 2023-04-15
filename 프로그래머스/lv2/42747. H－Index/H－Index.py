def solution(citations):
    n = len(citations)
    H = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(n):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i:
            H = max(H, i)
    return H