from collections import deque
def solution(priorities, location):
    answer = 0
    process_execution = 0
    q = deque()
    for idx, val in enumerate(priorities):
        q.append((idx, val))
    while q:
        idx, val = q.popleft()
        if any(val < v for i,v in q):
            # 반복문을 돌면서 자기자신보다 큰게 있으면 다시 넣는다
            q.append((idx, val))
        else:
            process_execution += 1
            if idx == location:
                answer = process_execution
                break
    return answer