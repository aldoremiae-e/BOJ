def solution(s):
    answer = 0
    def extend(left, right):
        while True:
            if left < 0 or right >= len(s):                
                break
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left+1:right]
            
    ret = ""
    for i in range(len(s)):
        ret = max(ret, extend(i, i), extend(i,i + 1), key = len)
    
    return len(ret)