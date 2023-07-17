from heapq import heapify, heappush, heappop
heap = []
N = int(input())
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        heappush(heap, l[j])
        if len(heap) > N:
            heappop(heap)
print(heap[0])