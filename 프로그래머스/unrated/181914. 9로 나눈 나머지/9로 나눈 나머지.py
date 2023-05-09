def solution(num):
    answer = 0
    l = len(num)
    for i in range(l):
        answer += int(num[i])
    answer = answer % 9
    return answer