def solution(n, s):
    # 곱이 최대가 되는 방법 : 집합의 수 간의 차이가 안나면 좋음
    if s // n == 0:
        return [-1]
    else:
        best = []
        while n > 0:
            best.append(s//n)
            s -= (s//n)
            n -= 1
            
        return best