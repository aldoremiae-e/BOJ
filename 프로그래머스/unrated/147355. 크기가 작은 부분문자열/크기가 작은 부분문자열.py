def solution(t, p):
    answer = 0
    l = len(p)
    nums = []
    
    for i in range(0, len(t) - l + 1):
        num = int(t[i:i+l])
        if num <= int(p):
            nums.append(num)
            
    answer = len(nums)
    
    '''
    while l <= len(t):
        k = l - len(p)
        num = int(t) % (10 ** l)
        nint = int(t) % (10 ** k)
        if int((num - nint) * (10 ** (-k))) <= int(p):
            answer += 1
        l += 1
    '''
    return answer