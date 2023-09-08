from collections import deque
def solution(n, k):
    answer = 0    
    # 소수분리
    def is_prime(m):
        if m == 1:
            return False
        for i in range(2, int(m**0.5)+1):
            if m % i == 0:
                return False
        return True

    # K진수변환
    q = deque()
    while n > k:
        q.appendleft(n % k)
        n = n // k
    q.appendleft(n)
    
    # 찾기
    num = 0
    while q:
        qnum = q.popleft()
        if qnum > 0:
            num *= 10
            num += qnum
        else:
            if num > 0:
                if is_prime(num):
                    answer += 1
                num = 0
    if num > 0:
        if is_prime(num):
            answer += 1
    return answer