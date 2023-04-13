from collections import deque

def solution(queue1, queue2):
    answer = 0
    a, b = sum(queue1), sum(queue2)
    snum = a + b
    target = snum // 2
    if a == b == target:
        answer = 0
        return answer
    q = queue1 + queue2
    l = len(q)
    idx1, idx2 = 0, len(queue1)
    flag = 0
    cnt = 1
    while cnt <= 600001:
        # 만약
        if idx2 == 0 and idx1 == len(queue1):
            flag = 0
            break
            
        if a < b:
            a += q[idx2]
            b -= q[idx2]
            idx2 = (idx2 + 1) % l
        elif a > b:
            a -= q[idx1]
            b += q[idx1]
            idx1 = (idx1 + 1) % l
        else:
            # 같다
            flag = 1
            break
        answer += 1
        cnt += 1
        
    if flag == 0:
        answer = -1
        return answer
    else:
        return answer