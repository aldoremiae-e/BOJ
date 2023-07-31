def solution(s):
    answer = ''
    lst = list(map(int, s.split()))
    maxans = max(lst)
    minans = min(lst)
    answer = str(minans) + ' ' + str(maxans)
    return answer