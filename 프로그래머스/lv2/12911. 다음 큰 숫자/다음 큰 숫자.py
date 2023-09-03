def solution(n):
    answer = 0
    # 이진수 변환
    # 1의 개수 세기
    def cnt_one(num):
        ret = 0
        while num > 1:
            if num % 2:
                ret += 1
            num //= 2
        return ret
    # 수의 증가
    
    cnt = cnt_one(n)
    while True:
        n += 1
        if cnt == cnt_one(n):
            answer = n
            break
    return answer