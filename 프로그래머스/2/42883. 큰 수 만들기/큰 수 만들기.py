def solution(number, k):
    answer = ''
    l = len(number) - k
    s, e = 0, l
    while True:
        if len(answer) == l:
            break
        max_num = 0
        max_idx = s
        for i in range(s, len(number)-e+1):
            if max_num < int(number[i]):
                max_num = int(number[i])
                max_idx = i
            if max_num == 9:
                break
        answer += str(max_num)
        s = max_idx + 1
        e -= 1
        k -= (max_idx - s)

    return answer