def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    check = -1
    for target in targets:
        if check <= target[0]:
            answer += 1
            check = target[1]
    return answer