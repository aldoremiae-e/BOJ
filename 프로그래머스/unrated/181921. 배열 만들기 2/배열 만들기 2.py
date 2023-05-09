def solution(l, r):
    answer = []
    for i in range(l, r+1):
        flag = True
        num = i
        while True:
            if num % 10 == 5 or num % 10 == 0:
                num //= 10
            else:
                flag = False
                break
            if num == 0:
                break
        if flag:      
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer