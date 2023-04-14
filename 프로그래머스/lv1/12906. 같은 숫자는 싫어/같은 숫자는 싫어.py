from collections import deque
def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    arr = deque(arr)
    while arr:
        a = arr.popleft()
        if not answer:
            answer.append(a)
        if a != answer[-1]:
            answer.append(a)
    return answer