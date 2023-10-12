def solution(want, number, discount):
    answer = 0
    want_dict = {}
    memo = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        memo[want[i]] = 0
    def check(memo):
        for key, val in memo.items():
            if want_dict[key] > val:
                return 0
        return 1
    # 초기화
    for i in range(10):
        if not discount[i] in memo:
            continue
        memo[discount[i]] += 1
    answer += check(memo)
    for i in range(1, len(discount)-9):
        if discount[i-1] in memo:
            memo[discount[i-1]] -= 1
        if discount[i+9] in memo:
            memo[discount[i+9]] += 1
        answer += check(memo)
    return answer