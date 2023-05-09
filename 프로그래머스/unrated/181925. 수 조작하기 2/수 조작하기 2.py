def solution(nums):
    answer = ''
    # 0 1 0 10 0 1 0 10 0 -1 -2 -1
    # w+1 s-1 d+10 a-10
    # wsdawsdassw
    
    for i in range(1, len(nums)):
        m = nums[i] - nums[i-1]
        if m == 1:
            answer += 'w'
        elif m == -1:
            answer += 's'
        elif m == 10:
            answer += 'd'
        else:
            answer += 'a'
            
    return answer