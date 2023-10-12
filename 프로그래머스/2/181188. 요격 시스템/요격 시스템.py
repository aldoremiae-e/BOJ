def solution(targets):
    answer = 0
    targets.sort()
    targets.append([100_000_000, 100_000_000])
    check = [-1, -1]
    for target in targets:
        if check[0] == -1 and check[1] == -1:
            check[0] = target[0] + 0.1
            check[1] = target[1] - 0.1
            continue
        if check[1] < target[0]:
            answer += 1
            check[0] = target[0] + 0.1
            check[1] = target[1] - 0.1
        else:
            check[0] = max(check[0], target[0]+0.1)
            check[1] = min(check[1], target[1]-0.1)
    return answer