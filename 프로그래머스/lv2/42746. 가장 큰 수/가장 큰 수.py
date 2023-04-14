def solution(numbers):
    answer = ''
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda num: num*3, reverse=True)
    
    for num in numbers:
        answer += num
    if int(answer) == 0:
        answer = "0"
    return answer