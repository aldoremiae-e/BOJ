def solution(k, d):
    global visit, answer, flag
    answer = -1
    l = len(d)
    visit = [False] * l
    flag = False
    def back_tracking(h, cnt):
        global answer, visit, flag
        if h < 0:
            return
        answer = max(answer, cnt)
        if answer == l:
            flag = True
            return
        for i in range(l):
            if visit[i]:
                continue
            if h >= d[i][0]:
                visit[i] = True
                back_tracking(h-d[i][1], cnt+1)
                visit[i] = False
            if flag:
                return
    back_tracking(k, 0)
    return answer