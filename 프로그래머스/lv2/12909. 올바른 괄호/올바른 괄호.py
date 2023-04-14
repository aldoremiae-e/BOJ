from collections import deque
def solution(s):
    answer = True
    lst = deque()
    for i in range(len(s)):
            lst.append(s[i])
    q = deque()
    flag = 1
    while lst:
        a = lst.popleft()
        if a == '(':
            q.append(a)
        else:
            if not q:
                flag = 0
                break
            q.pop()

    if q or flag == 0:
        answer = False
    else:
        answer = True
                
    return answer