from collections import deque
def solution(progresses, speeds):
    answer = []
    stack = []
    cnt = 0
    for i in range(len(speeds)):
        if (100 - progresses[i])  % speeds[i]:
            day = (100 - progresses[i]) // speeds[i] + 1
        else:
            day = (100 - progresses[i])// speeds[i]
        if not stack:
            stack.append(day)
            cnt += 1
        else:
            if day <= stack[-1]:
                # 스택에 추가하지 않고 개수 추가
                cnt += 1
            else:
                # 스택에 추가하고 개수 초기화
                stack.append(day)
                answer.append(cnt)
                cnt = 1
    answer.append(cnt)
            
            
    return answer