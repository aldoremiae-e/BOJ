def solution(money):
    answer = 0
    N = len(money)
    if N == 3:
        return max(money)
    memo1 = [0] * N
    memo2 = [0] * N
    memo1[0] = money[0]
    memo1[2] = money[2] + memo1[0]
    memo2[1] = money[1]
    
    for i in range(3, N):
        memo1[i] = max(memo1[i-2], memo1[i-3]) + money[i]
        memo2[i] = max(memo2[i-2], memo2[i-3]) + money[i]
        if i == N-1:
            memo1[i] -= memo1[0]
    answer = max(max(memo1), max(memo2))
    return answer