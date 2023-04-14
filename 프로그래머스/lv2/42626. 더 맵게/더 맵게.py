from heapq import heappop, heappush, heapify
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heappush(heap, i)
    while heap[0] < K:
        try:
            heappush(heap, heappop(heap) + heappop(heap) * 2)
        except IndexError:
            return -1
        answer += 1
    return answer