def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        check = []
        for i in range(s, e+1):
            if arr[i] > k:
                check.append(arr[i])
        if check:
            answer.append(min(check))
        else:
            answer.append(-1)
    return answer