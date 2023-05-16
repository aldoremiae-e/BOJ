def solution(my_string, s, e):
    answer = ''
    # s미만
    front = my_string[:s]
    re = my_string[s:e+1]
    answer = front + re[::-1] + my_string[e+1:]
    return answer