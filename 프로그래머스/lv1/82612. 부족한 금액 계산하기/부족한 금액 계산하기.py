def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        t = (price * i)
        answer += t
    if answer >= money:
        answer -= money
    else:
        answer = 0
    return answer