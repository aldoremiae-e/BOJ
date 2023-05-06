def solution(my_string, overwrite_string, s):
    answer = ''
    l = len(overwrite_string)
    answer += my_string[:s]
    answer += overwrite_string
    answer += my_string[s+l:]
    return answer