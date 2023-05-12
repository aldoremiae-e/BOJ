from heapq import heappop, heappush
def solution(scov, K):
    answer = 0
    heap = []
    for i in scov:
        heappush(heap, i)
    while heap[0] < K:
        n = heappop(heap) + (heappop(heap) * 2)
        heappush(heap, n)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer