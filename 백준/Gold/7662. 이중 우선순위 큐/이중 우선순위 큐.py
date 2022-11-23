from heapq import heappop, heappush
from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    maxlst = []
    minlst = []
    visited = [0] * k
    for i in range(k):
        op = stdin.readline()
        order = op[0]
        num = int(op[2:])

        if order == 'I':
            heappush(maxlst, (-num, i))
            heappush(minlst, (num, i))
            
        elif order == 'D':
            if num > 0:
                while maxlst:
                  if visited[maxlst[0][1]] == 1:
                    heappop(maxlst)
                  else:
                    break
                if maxlst and visited[maxlst[0][1]] == 0 :
                  visited[maxlst[0][1]] = 1
                  heappop(maxlst)
                    
            elif num < 0:
                # 최소값 - heappop은 최소값 빠짐
                while minlst:
                  if visited[minlst[0][1]] == 1:
                    heappop(minlst)
                  else:
                    break
                  
                if minlst and visited[minlst[0][1]] == 0 :
                  visited[minlst[0][1]] = 1
                  heappop(minlst)
    while maxlst:
      if visited[maxlst[0][1]] == 1:
        heappop(maxlst)
      else:
        break
    while minlst:
      if visited[minlst[0][1]] == 1:
        heappop(minlst)
      else:
        break
    
    if maxlst and minlst:
      print(-maxlst[0][0], minlst[0][0])
    else:
      print('EMPTY')