from heapq import heappush, heappop
def solution(O):
    answer = []
    l = len(O)
    h = []
    for i in range(l):
        op, n = O[i][0], int(O[i][2:])
        
        if op == 'I':
            # 삽입
            heappush(h, n)
        elif op == 'D':
            # 삭제
            if not h:
                continue
                
            if n > 0:
                # 최댓값 삭제
                m = max(h)
                h.remove(m)
            else:
                # 최솟값 삭제
                heappop(h)

    if h:
        answer = [max(h), min(h)]
    else:
        answer = [0, 0]
    return answer