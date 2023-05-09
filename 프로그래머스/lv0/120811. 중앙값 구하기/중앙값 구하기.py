def solution(array):
    answer = 0
    a = sorted(array)
    answer = a[len(a)//2]
    return answer