from heapq import heappop, heappush
def solution(n, works):
    answer = 0
    if sum(works) < n:
        return answer
    heap = []
    for i in works:
        heappush(heap, -i)
    while n > 0:
        num = heappop(heap)
        heappush(heap, num+1)
        n -= 1
    for i in heap:
        answer += i ** 2
    return answer