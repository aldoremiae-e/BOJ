from heapq import heapify, heappush, heappop
N = int(input())
heap = []
dasom = int(input())
dasom *= -1
cnt = 0
for i in range(2, N+1):
    n = int(input())
    heappush(heap, [-n, i])
if heap:
    while True:
        if heap[0][0] > dasom:
            break
        curn, curi = heappop(heap)
        heappush(heap, [curn+1, curi])
        dasom -= 1
        cnt += 1
print(cnt)